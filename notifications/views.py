from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NotificationSerializer, OptionSerializer
from .models import Notification, Option


@api_view(['POST', ])
def create_notification(request):
    user = request.user

    notification = Notification(userId=user)

    if request.method == 'POST':
        serializer = NotificationSerializer(notification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def create_option(request, pk):
    option = Option(notificationId=pk)
    if request.method == 'POST':
        serializer = OptionSerializer()
