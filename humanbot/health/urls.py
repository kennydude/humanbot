from django.conf.urls import url, include

from humanbot.health.views import WithingsImporter


urlpatterns = [
    url(r'^withings-import/$', WithingsImporter.as_view(),
        name='withings-import'),
]
