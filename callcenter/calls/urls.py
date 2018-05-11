from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^calls$', views.CallViewSet.as_view(), name='calls'),
]
