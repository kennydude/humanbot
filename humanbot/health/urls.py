from django.conf.urls import url, include

from humanbot.health.views import (WithingsImporter, WithingsConnect,
    RunkeeperConnectView, RunkeeperSyncView)


urlpatterns = [
    url(r'^withings-import/$',
        WithingsImporter.as_view(),
        name='withings-import'),
    url(r'^runkeeper-import/$',
        RunkeeperSyncView.as_view(),
        name='runkeeper-import'),
    url(r'^profile/(?P<pk>[0-9]+)/services/withings/connect',
        WithingsConnect.as_view(),
        name='withings-connect'),
    url(r'^profile/(?P<pk>[0-9]+)/services/runkeeper/connect',
        RunkeeperConnectView.as_view(),
        name='runkeeper-connect'),
]
