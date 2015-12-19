from django.contrib.gis.db import models

from humanbot.health.models.measurements import Measurement


class RouteMeasurement(models.Model):
    measurement = models.ForeignKey(Measurement)
    route = models.MultiPointField()

    def __unicode__(self):
        return 'Geo for {}'.format(self.measurement)
