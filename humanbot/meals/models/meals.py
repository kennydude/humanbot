'''Describes actual meals and ingredients if applicable
'''
from django.db import models

from humanbot.core.models import Human


class Ingredient(models.Model):
    human = models.ForeignKey(Human)
    name = models.CharField(max_length=200)


class Meal(models.Model):
    human = models.ForeignKey(Human)
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient, related_name='meals')
    recipe = models.TextField()
