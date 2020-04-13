from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response

from .serializers import NotificationSerializer
from rest_framework.decorators import api_view
from .models import Notification

@api_view(['POST', ])
def create_notification(request):
    user = request.user

    notification = Notification(user=user)

    if request.method == 'POST':
        serializer = NotificationSerializer(notification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
