from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^calls$', views.CallViewSet.as_view(), name='calls'),
    url(r'^bill/(?P<source>[0-9]+)/(?P<month>[0-9]+)/(?P<year>[0-9]+)/$',
        views.BillViewSet.as_view(), name='bill'),
]
