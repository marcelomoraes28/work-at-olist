from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Bill
from .serializers import CallSerializer, BillSerializer


class CallViewSet(APIView):
    """
    This endpoint presents calls
    """

    def post(self, request, format=None):
        """
        Parameters
        ----------
        {
            "source" : `integer`
            "destination": `integer`
            "type": `integer` (1 - Start a call, 2 - Terminate a call)
            "call_id": `integer` (Unique identifier)
            "timestamp": `datetime`
        }
        ----------
        Example to start a call:
        ----------
        {
            "source" : 41997471140
            "destination": 41997471120
            "type": 1
            "call_id": 1
            "timestamp": "2018-05-02 10:10:10"
        }
        ----------
        Example to terminate a call:
        ----------
        {
            "type": 2
            "call_id": 1
            "timestamp": "2018-05-02 10:15:10"
        }
        """
        call_serializer = CallSerializer(data=request.data)
        if call_serializer.is_valid():
            call_serializer.save()
            return Response(call_serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(call_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class BillViewSet(APIView):
    """
    This endpoint presents Bills
    """

    def _get_bill_objects(self, source, month, year):
        bills = Bill.objects.filter(source=source,
                                    call_start_date__year__gte=year,
                                    call_start_date__month__gte=month)
        if not bills:
            raise Http404
        return bills

    def get(self, request, source, month, year):
        """
        Parameters
        ----------
        source/month/year

        ----------
        Example to get a bill:
        ----------
        calls/bill/10/2018
        """
        bill = self._get_bill_objects(source, month, year)
        serializer = BillSerializer(bill, many=True)
        return Response(serializer.data)
