from django.db import models

from humanbot.core.models import Human


class MeasurementGroup(models.Model):
    """For example a workout or event
    """
    name = models.CharField(max_length=150)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    group_type = models.CharField(max_length=50)

    def __unicode__(self):
        return '{}: {}'.format(self.group_type, self.name)


class MeasurementType(models.Model):
    """Used for normalising measurements
    """
    name = models.CharField(max_length=50)
    factor = models.IntegerField(help_text="""
What is the factor of this measurement in order to standardise it.<br/>
For example: "Length of pool" here may have a factor of
25, so another pool of 50 will not skew measurements wildly
""")

    def __unicode__(self):
        return '{} (factor: {})'.format(self.name, self.factor)


class MeasurementFor(models.Model):
    """What is the measurement for? Swimming? Weight?
    """
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Measurement(models.Model):
    """An actual measurement
    """
    human = models.ForeignKey(Human)
    created = models.DateTimeField()
    value = models.IntegerField()
    measurement_type = models.ForeignKey(MeasurementType)
    measurement_for = models.ForeignKey(MeasurementFor)
    grouping = models.ForeignKey(MeasurementGroup, null=True, blank=True)

    source_name = models.CharField(max_length=50, default='manual')
    source_id = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return '{} on {} for {} of type {}'.format(
            self.value, self.created, self.measurement_for,
            self.measurement_type)
