from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from rest_framework import viewsets

from humanbot.core.models import Human
from humanbot.core.serializers import HumanSerializer


class HumanView(DetailView):
    template_name = 'core/human.html'
    model = Human


class HumanListView(viewsets.ModelViewSet):
    serializer_class = HumanSerializer

    def get_queryset(self):
        return Human.objects.filter(connection__user=self.request.user)


class AppView(TemplateView):
    template_name = 'core/app.html'
