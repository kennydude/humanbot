from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from humanbot.health.models import Measurement, RouteMeasurement


class MeasurementSerializer(serializers.ModelSerializer):
    normalised_value = serializers.SerializerMethodField()
    human_id = serializers.IntegerField()
    has_route = serializers.SerializerMethodField()

    def get_normalised_value(self, obj):
        return obj.value * obj.measurement_type.factor

    def get_has_route(self, obj):
        return obj.route.exists()

    class Meta:
        model = Measurement
        fields = ['id', 'human_id', 'created', 'value',
                  'source_name', 'source_id', 'has_route',
                  'normalised_value']


class RouteMeasurementSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RouteMeasurement
        geo_field = 'route'
