from django.conf.urls import url, include

from humanbot.core.views import (HumanView, HumanListView, AppView)


urlpatterns = [
    url(r'^humans/$',
        HumanListView.as_view()),
    url(r'^humans/(?P<pk>[0-9]+)/$',
        HumanView.as_view()),
    url(r'^app/$',
        AppView.as_view())
]
