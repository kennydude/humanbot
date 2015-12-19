from django.http import HttpResponse
from django.conf import settings
from requests_oauthlib import OAuth1Session
import oauthlib.oauth1
import datetime
import json

from django.views.generic import View
from django.shortcuts import redirect
from humanbot.health.models import Measurement, MeasurementType, MeasurementFor
from humanbot.core.models import ConnectedService

# Map these to our own values
# you can customize more details on these in admin! (except name for now)
MEASUREMENT_FORS = {
    1: 'Weight',
    4: 'Height',
    5: 'Fat Free Mass',
    6: 'Fat Ratio',
    8: 'Fat Mass Weight',
    9: 'Diastolic Blood Pressure',
    10: 'Systolic Blood Pressure',
    11: 'Heart Pulse',
    54: 'SPO2',
}
MEASUREMENT_TYPES = {
    1: 'Kilograms',
    4: 'Height',
    5: 'Kilograms',
    6: 'Percentage',
    8: 'Percentage',
    9: 'Millimeter of mercury',
    10: 'Millimeter of mercury',
    11: 'Beats per minute',
    54: 'Percentage'
}


class WithingsImporter(View):
    def get(self, *args):
        providers = ConnectedService.objects.filter(service_name='withings')
        for provider in providers:
            extra_data = json.loads(provider.auth_details)
            token = extra_data['oauth_token']
            secret = extra_data['oauth_token_secret']

            withings = OAuth1Session(
                client_key=settings.SOCIAL_AUTH_WITHINGS_KEY,
                client_secret=settings.SOCIAL_AUTH_WITHINGS_SECRET,
                resource_owner_key=token,
                resource_owner_secret=secret,
                signature_type=oauthlib.oauth1.SIGNATURE_TYPE_QUERY)

            url = "https://wbsapi.withings.net/measure?action=getmeas&userid={}"
            url = url.format(extra_data['userid'])
            rsp = withings.get(url)
            body = rsp.json()
            assert body['status'] == 0

            for data in body['body']['measuregrps']:
                if data['category'] != 1:
                    continue  # Real data only please!

                for measure in data['measures']:
                    measurement_for = MeasurementFor.objects.get_or_create(
                        name=MEASUREMENT_FORS[measure['type']])[0]
                    measurement_type = MeasurementType.objects.get_or_create(
                        name=MEASUREMENT_TYPES[measure['type']],
                        defaults={
                            'factor': 1
                        })[0]
                    Measurement.objects.get_or_create(
                        source_id='{}_{}'.format(
                            data['grpid'], measure['type']),
                        source_name='withings',
                        human=provider.human,
                        defaults={
                            'value':
                                measure['value'] * pow(10, measure['unit']),
                            'created':
                                datetime.datetime.fromtimestamp(data['date']),
                            'measurement_for': measurement_for,
                            'measurement_type': measurement_type,
                        })
        return HttpResponse('ok')


class WithingsConnect(View):
    def get(self, *args, **kwargs):
        access_token_url = 'https://oauth.withings.com/account/access_token'
        request_token_url = 'https://oauth.withings.com/account/request_token'
        authorization_base_url = 'https://oauth.withings.com/account/authorize'

        if 'oauth_verifier' in self.request.GET:
            service = ConnectedService.objects.get(service_name='withings',
                                                   human_id=kwargs['pk'])
            s_data = json.loads(service.auth_details)
            withings = OAuth1Session(
                client_key=settings.SOCIAL_AUTH_WITHINGS_KEY,
                client_secret=settings.SOCIAL_AUTH_WITHINGS_SECRET,
                resource_owner_key=s_data['oauth_token'],
                resource_owner_secret=s_data['oauth_token_secret'],
                verifier=self.request.GET['oauth_verifier'])

            token = withings.fetch_access_token(access_token_url)
            service.auth_details = json.dumps(token)
            service.save()
            return redirect('/profile/{}'.format(kwargs['pk']))

        redirect_url = self.request.build_absolute_uri()
        withings = OAuth1Session(
            client_key=settings.SOCIAL_AUTH_WITHINGS_KEY,
            client_secret=settings.SOCIAL_AUTH_WITHINGS_SECRET,
            callback_uri=redirect_url)

        token = withings.fetch_request_token(request_token_url)
        ConnectedService.objects.create(human_id=kwargs['pk'],
                                        service_name='withings',
                                        auth_details=json.dumps(token))

        url = withings.authorization_url(authorization_base_url)

        return redirect(url)
