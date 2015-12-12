from django.contrib import admin

from humanbot.health.models import (Measurement, MeasurementType,
        MeasurementGroup, MeasurementFor)
# Register your models here.

admin.site.register(Measurement)
admin.site.register(MeasurementType)
admin.site.register(MeasurementGroup)
admin.site.register(MeasurementFor)
