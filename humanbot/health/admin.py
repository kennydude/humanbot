from django.contrib.gis import admin

from humanbot.health.models import (Measurement, MeasurementType,
        MeasurementGroup, MeasurementFor, RouteMeasurement)
# Register your models here.

admin.site.register(Measurement)
admin.site.register(MeasurementType)
admin.site.register(MeasurementGroup)
admin.site.register(MeasurementFor)
admin.site.register(RouteMeasurement, admin.OSMGeoAdmin)
