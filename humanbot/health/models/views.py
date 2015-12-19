from django.db import models

from django_pgviews import view as pg

from humanbot.core.models import Human
from humanbot.health.models import (MeasurementFor, MeasurementGroup,
    MeasurementType)


class NormalisedMeasurement(pg.View):
    sql = """SELECT
    m.id,
    m.created,
    m.value * t.factor AS value,
    m.source_name,
    m.source_id,
    m.grouping_id,
    m.human_id,
    m.measurement_type_id,
    m.measurement_for_id
FROM health_measurement m
INNER JOIN health_measurementtype t ON t.id = m.measurement_type_id"""

    human = models.ForeignKey(Human)
    created = models.DateTimeField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    measurement_type = models.ForeignKey(MeasurementType)
    measurement_for = models.ForeignKey(MeasurementFor)
    grouping = models.ForeignKey(MeasurementGroup, null=True, blank=True)

    source_name = models.CharField(max_length=50, default='manual')
    source_id = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
