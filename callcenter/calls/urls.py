from django.conf.urls import include, url
from rest_framework import routers

from . import views

urlpatterns = [
    url(r'^calls$', views.CallViewSet.as_view(), name='calls'),
]
