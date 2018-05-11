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
            "call_type": `integer` (1 - Start a call, 2 - Terminate a call)
            "call_id": `integer` (Unique identifier)
            "timestamp": `datetime`
        }
        ----------
        Example to start a call:
        ----------
        {
            "source" : 41997471140
            "destination": 41997471120
            "call_type": 1
            "call_id": 1
            "timestamp": "2018-05-02 10:10:10"
        }
        ----------
        Example to terminate a call:
        ----------
        {
            "call_type": 2
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

    def get(self, request, format=None):
        """
        List all bills
        """
        bill = Bill.objects.all()
        serializer = BillSerializer(bill, many=True)
        return Response(serializer.data)
