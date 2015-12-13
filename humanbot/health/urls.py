from django.conf.urls import url, include

from humanbot.health.views import WithingsImporter, WithingsConnect


urlpatterns = [
    url(r'^withings-import/$', WithingsImporter.as_view(),
        name='withings-import'),
    url(r'^profile/(?P<pk>[0-9]+)/services/withings/connect',
        WithingsConnect.as_view(), name='withings-connect'),
]
