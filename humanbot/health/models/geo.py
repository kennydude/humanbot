from django.contrib.gis.db import models

from humanbot.health.models.measurements import Measurement


class RouteMeasurement(models.Model):
    measurement = models.ForeignKey(Measurement, related_name='route')
    route = models.LineStringField()

    def __unicode__(self):
        return 'Geo for {}'.format(self.measurement)
