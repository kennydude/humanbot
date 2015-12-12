from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Human(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.name
