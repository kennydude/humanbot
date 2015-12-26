from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Human(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField()

    def __unicode__(self):
        return self.name

    def get_connected_services(self):
        services = list(ConnectedService.objects.filter(
            human=self).values_list('service_name', flat=True))
        return {
            'withings': {
                'name': 'Withings',
                'key': 'withings',
                'connected': 'withings' in services
            },
            'runkeeper': {
                'name': 'Runkeeper',
                'key': 'runkeeper',
                'connected': 'runkeeper' in services
            }
        }


class HumanUserConnection(models.Model):
    human = models.ForeignKey(Human, related_name='connection')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    can_write = models.BooleanField(default=False)

    def __unicode__(self):
        if self.can_write:
            return '{} can write to {}'.format(self.user, self.human)
        else:
            return '{} can read from {}'.format(self.user, self.human)


class ConnectedService(models.Model):
    service_name = models.CharField(max_length=200)
    auth_details = models.TextField()
    human = models.ForeignKey(Human)

    def __unicode__(self):
        return '{} for {}'.format(self.service_name, self.human)
