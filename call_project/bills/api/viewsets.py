from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import BillSerializer
from bills.models import Bill


class BillViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents Bills
    """
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def get_queryset(self):
        source = self.kwargs['source']
        if 'month' and 'year' in self.kwargs:
            month = self.kwargs['month']
            year = self.kwargs['year']
            return Bill.objects.filter(source=source,
                                       call_start_date__year__gte=year,
                                       call_start_date__month__gte=month
                                       )
        return [Bill.objects.filter(source=source).first()]
