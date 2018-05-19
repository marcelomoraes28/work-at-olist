from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, mixins

from .serializers import CallSerializer
from calls.models import Call


class CallViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    """
    This endpoint presents calls
    """
    queryset = Call.objects.all()
    serializer_class = CallSerializer

    def create(self, request, *args, **kwargs):
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
            # Save a Call
            call_serializer.save()
            return Response(call_serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(call_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
