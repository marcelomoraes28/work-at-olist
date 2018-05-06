from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CallSerializer


class CallViewSet(APIView):
    """
    CallViewSet
    """
    def post(self, request, format=None):
        """
        Create a new register
        :param request:
        :param format:
        :return:
        """
        call_serializer = CallSerializer(data=request.data)
        if call_serializer.is_valid():
            call_serializer.save()
            return Response(call_serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(call_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
