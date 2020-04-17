from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NotificationSerializer, OptionSerializer
from .models import Notification, Option
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

notification_response = openapi.Response('response description', NotificationSerializer)
option_response = openapi.Response('response description', OptionSerializer)

@swagger_auto_schema(method='get',
    responses={
        '200': notification_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET', ])
def get_notification(request, pk):
    try:
        notification = Notification.objects.get(id=pk)
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)

@swagger_auto_schema(method='get',
    responses={
        '200': option_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET', ])
def get_option(request, pk):
    try:
        option = Option.objects.get(id=pk)
    except Option.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OptionSerializer(option)
        return Response(serializer.data)


@swagger_auto_schema(method='post', request_body=NotificationSerializer,
    responses={
        '201': 'Created',
        '400': 'Bad Request',
        '401': 'Unauthorized',
    })
@api_view(['POST', ])
def create_notification(request):
    user = request.user

    notification = Notification(user=user)

    if request.method == 'POST':
        serializer = NotificationSerializer(notification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=OptionSerializer,
    responses={
        '201': 'Created',
        '400': 'Bad Request',
        '401': 'Unauthorized',
    })
@api_view(['POST', ])
def create_option(request, pk):
    notification = Notification.objects.get(id=pk)
    option = Option(notification=notification)

    if request.method == 'POST':
        serializer = OptionSerializer(option, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='put', request_body=NotificationSerializer,
    responses={
        '200': 'Success',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['PUT', ])
def update_notification(request, pk):
    try:
        notification = Notification.objects.get(id=pk)
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = NotificationSerializer(notification, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=OptionSerializer,
    responses={
        '200': 'Success',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['PUT', ])
def update_option(request, pk):
    try:
        option = Option.objects.get(id=pk)
    except Option.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OptionSerializer(option, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete',
    responses={
        '200': 'Success',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['DELETE', ])
def delete_notification(request, pk):
    try:
        notification = Notification.objects.get(id=pk)
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = notification.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)

@swagger_auto_schema(method='delete',
    responses={
        '200': 'Success',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['DELETE', ])
def delete_option(request, pk):
    try:
        option = Option.objects.get(id=pk)
    except Option.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = option.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)
