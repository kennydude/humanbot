import urllib
import json
import datetime

from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.gis.geos import MultiPoint, Point

import requests
import arrow

from humanbot.core.models import ConnectedService
from humanbot.health.models import (Measurement, MeasurementType,
    MeasurementFor, RouteMeasurement)


class RunkeeperSyncView(View):
    '''Sync down activities from Runkeeper
    '''
    def get(self, *args, **kwargs):
        providers = ConnectedService.objects.filter(service_name='runkeeper')
        for provider in providers:
            extra_data = json.loads(provider.auth_details)
            access_token = extra_data['access_token']
            r = requests.get("https://api.runkeeper.com/fitnessActivities",
                headers={
                    'Authorization': 'Bearer {}'.format(access_token)
                }).json()

            m_type = MeasurementType.objects.get_or_create(
                name='Meters',
                defaults={
                    'factor': 1
                }
            )[0]

            for activity in r['items']:
                m_for = MeasurementFor.objects.get_or_create(
                    name=activity['type'])[0]
                measure, created = Measurement.objects.get_or_create(
                    source_id='{}_{}'.format(provider.human_id,
                        activity['uri']),
                    source_name='runkeeper',
                    human_id=provider.human_id,
                    defaults={
                        'measurement_for': m_for,
                        'measurement_type': m_type,
                        'value': activity['total_distance'],
                        'created': arrow.get(
                            activity['start_time'][5:].strip(), 'DD MMM YYYY HH:mm:ss').datetime
                    })
                if created:  # New!
                    print activity['uri'], 'is new'
                    m_body = requests.get("https://api.runkeeper.com{}".format(
                        activity['uri']), headers={
                            'Authorization': 'Bearer {}'.format(access_token)
                        }).json()
                    points = []
                    for point in m_body['path']:
                        points.append(Point(point['longitude'],
                            point['latitude']))
                    rm = RouteMeasurement(
                        route=MultiPoint(points),
                        measurement=measure)
                    rm.save()
        return HttpResponse('ok')


class RunkeeperConnectView(View):
    '''Connect to the Runkeeper service
    '''

    def get(self, *args, **kwargs):
        authorize_url = 'https://runkeeper.com/apps/authorize?{}'
        token_url = 'https://runkeeper.com/apps/token'
        redirect_url = self.request.build_absolute_uri()
        if '?' in redirect_url:
            redirect_url = redirect_url[:redirect_url.find('?')]

        if 'code' not in self.request.GET:
            # authorize
            return redirect(authorize_url.format(urllib.urlencode({
                'client_id': settings.RUNKEEPER_KEY,
                'response_type': 'code',
                'redirect_uri': redirect_url
            })))
        else:
            r = requests.post(token_url, data={
                'grant_type': 'authorization_code',
                'code': self.request.GET.get('code', None),
                'client_id': settings.RUNKEEPER_KEY,
                'client_secret': settings.RUNKEEPER_SECRET,
                'redirect_uri': redirect_url
            })
            b = r.json()
            if 'error' in b:
                raise Exception('Runkeeper error {}'.format(json.dumps(b)))
            ConnectedService.objects.update_or_create(
                human_id=kwargs['pk'],
                service_name='runkeeper',
                defaults={
                    'auth_details': json.dumps(b)
                })
            return redirect('/profile/{}'.format(kwargs['pk']))
