from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Bill, TYPES
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
        bill_serializer = BillSerializer(data=request.data)
        if bill_serializer.is_valid():
            # Save a Bill
            bill_serializer.save()
        else:
            return Response(bill_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        request.data['call_id'] = bill_serializer.data
        call_serializer = CallSerializer(data=request.data)
        if call_serializer.is_valid():
            # Save a Call
            call_serializer.save()
            return Response(call_serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(call_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


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
