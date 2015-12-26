from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from humanbot.core.models import Human


class HumanView(DetailView):
    template_name = 'core/human.html'
    model = Human


class HumanListView(ListView):
    def get_queryset(self):
        return Human.objects.filter(connection__user=self.request.user)


class AppView(TemplateView):
    template_name = 'core/app.html'
