from django.db import models

from humanbot.meals.models.meals import Meal
from humanbot.core.models import Human


class MealPlan(models.Model):
    '''A meal plan for a week
    '''
    human = models.ForeignKey(Human)
    week_commencing = models.DateField()

    monday_breakfast = models.ForeignKey(Meal,
        related_name='plan_monday_breakfast')
    monday_lunch = models.ForeignKey(Meal,
        related_name='plan_monday_lunch')
    monday_dinner = models.ForeignKey(Meal,
        related_name='plan_monday_dinner')

    tuesday_breakfast = models.ForeignKey(Meal,
        related_name='plan_tuesday_breakfast')
    tuesday_lunch = models.ForeignKey(Meal,
        related_name='plan_tuesday_lunch')
    tuesday_dinner = models.ForeignKey(Meal,
        related_name='plan_tuesday_dinner')

    wednesday_breakfast = models.ForeignKey(Meal,
        related_name='plan_wednesday_breakfast')
    wednesday_lunch = models.ForeignKey(Meal,
        related_name='plan_wednesday_lunch')
    wednesday_dinner = models.ForeignKey(Meal,
        related_name='plan_wednesday_dinner')

    thursday_breakfast = models.ForeignKey(Meal,
        related_name='plan_thursday_breakfast')
    thursday_lunch = models.ForeignKey(Meal,
        related_name='plan_thursday_lunch')
    thursday_dinner = models.ForeignKey(Meal,
        related_name='plan_thursday_dinner')

    friday_breakfast = models.ForeignKey(Meal,
        related_name='plan_friday_breakfast')
    friday_lunch = models.ForeignKey(Meal,
        related_name='plan_friday_lunch')
    friday_dinner = models.ForeignKey(Meal,
        related_name='plan_friday_dinner')

    saturday_breakfast = models.ForeignKey(Meal,
        related_name='plan_saturday_breakfast')
    saturday_lunch = models.ForeignKey(Meal,
        related_name='plan_saturday_lunch')
    saturday_dinner = models.ForeignKey(Meal,
        related_name='plan_saturday_dinner')

    sunday_breakfast = models.ForeignKey(Meal, 
        related_name='plan_sunday_breakfast')
    sunday_lunch = models.ForeignKey(Meal,
        related_name='plan_sunday_lunch')
    sunday_dinner = models.ForeignKey(Meal,
        related_name='plan_sunday_dinner')
