from __future__ import unicode_literals

from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField()

    def __unicode__(self):
        return self.name
