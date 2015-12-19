from humanbot.health.serializers import (MeasurementSerializer,
    RouteMeasurementSerializer)
from humanbot.health.models import Measurement, RouteMeasurement

from rest_framework import viewsets


class MeasurementViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Measurement.objects.filter(
            human_id=self.kwargs['human_id']).prefetch_related(
            'measurement_type', 'route').order_by('-created')
    serializer_class = MeasurementSerializer
    filter_fields = ('measurement_for',)


class RouteViewSet(viewsets.ModelViewSet):
    """Returns a GeoJSON format of the route for the measurement
    """
    def get_object(self):
        return RouteMeasurement.objects.get(measurement_id=self.kwargs['pk'])
    serializer_class = RouteMeasurementSerializer
