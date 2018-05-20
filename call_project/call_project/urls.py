from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from calls.api.viewsets import CallViewSet
from bills.api.viewsets import BillViewSet

schema_view = get_swagger_view(title='Pastebin API')

router = routers.DefaultRouter()

router.register(r'calls', CallViewSet, base_name='calls')
router.register(r'bill/(?P<source>\w+)',
                BillViewSet, base_name='bills')
router.register(r'bill/(?P<source>\w+)/(?P<month>\w+)/(?P<year>\w+)',
                BillViewSet, base_name='bills_detail')
urlpatterns = [
    path('admin', admin.site.urls),
    path('docs', schema_view)
]

urlpatterns += router.urls
