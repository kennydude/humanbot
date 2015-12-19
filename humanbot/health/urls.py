from django.conf.urls import url, include

from humanbot.health.views import (WithingsImporter, WithingsConnect,
    RunkeeperConnectView, RunkeeperSyncView, MeasurementViewSet, RouteViewSet)


urlpatterns = [
    url(r'^withings-import/$',
        WithingsImporter.as_view(),
        name='withings-import'),
    url(r'^runkeeper-import/$',
        RunkeeperSyncView.as_view(),
        name='runkeeper-import'),
    url(r'^profile/(?P<pk>[0-9]+)/services/withings/connect$',
        WithingsConnect.as_view(),
        name='withings-connect'),
    url(r'^profile/(?P<pk>[0-9]+)/services/runkeeper/connect$',
        RunkeeperConnectView.as_view(),
        name='runkeeper-connect'),
    url(r'^api/humans/(?P<human_id>[0-9]+)/measurements$',
        MeasurementViewSet.as_view({
            'get': 'list'
        })),
    url(r'^api/humans/(?P<human_id>[0-9]+)/measurements/(?P<pk>[0-9]+)$',
        MeasurementViewSet.as_view({
            'get': 'retrieve'
        })),
    url(r'^api/humans/(?P<human_id>[0-9]+)/measurements/(?P<pk>[0-9]+)/route$',
        RouteViewSet.as_view({
            'get': 'retrieve'
        })),
]
