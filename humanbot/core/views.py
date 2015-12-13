from django.shortcuts import render
from django.views.generic import DetailView
from humanbot.core.models import Human


class HumanView(DetailView):
    template_name = 'core/human.html'
    model = Human
