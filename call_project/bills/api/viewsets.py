from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from call_project.calls.api.serializers import BillSerializer
from call_project.calls.models import Bill


class BillViewSet(APIView):
    """
    This endpoint presents Bills
    """

    @staticmethod
    def _get_bill_objects(source, year, month):
        if year and month:
            bills = Bill.objects.filter(source=source,
                                        call_start_date__year__gte=year,
                                        call_start_date__month__gte=month)
        else:
            bills = Bill.objects.filter(source=source).first()
        if not bills:
            raise Http404
        return bills

    def get(self, request, source, year='', month=''):
        """
        Parameters
        ----------
        source/month/year

        ----------
        Example to get a bill:
        ----------
        calls/bill/10/2018
        """
        bill = self._get_bill_objects(source, year, month)
        serializer = BillSerializer(bill, many=True)
        return Response(serializer.data)
