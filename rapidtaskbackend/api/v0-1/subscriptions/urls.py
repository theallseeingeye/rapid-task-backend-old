from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^subscriber/create/$', views.SubscriberCreate.as_view()),
    url(r'^subscriber/list/$', views.SubscriberList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
