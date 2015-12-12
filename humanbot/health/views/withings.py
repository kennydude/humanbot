from django.http import HttpResponse
from django.conf import settings
from requests_oauthlib import OAuth1Session
import oauthlib.oauth1
import datetime

from django.views.generic import View
from humanbot.health.models import Measurement, MeasurementType, MeasurementFor
from social.apps.django_app.default.models import UserSocialAuth

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
        providers = UserSocialAuth.objects.filter(provider='withings')
        for provider in providers:
            token = provider.extra_data['access_token']['oauth_token']
            secret = provider.extra_data['access_token']['oauth_token_secret']

            withings = OAuth1Session(
                client_key=settings.SOCIAL_AUTH_WITHINGS_KEY,
                client_secret=settings.SOCIAL_AUTH_WITHINGS_SECRET,
                resource_owner_key=token,
                resource_owner_secret=secret,
                signature_type=oauthlib.oauth1.SIGNATURE_TYPE_QUERY)

            url = "https://wbsapi.withings.net/measure?action=getmeas&userid={}"
            url = url.format(
                provider.extra_data['access_token']['userid'])
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
                        human=provider.user.human,
                        defaults={
                            'value':
                                measure['value'] * pow(10, measure['unit']),
                            'created':
                                datetime.datetime.fromtimestamp(data['date']),
                            'measurement_for': measurement_for,
                            'measurement_type': measurement_type,
                        })
        return HttpResponse('ok')
