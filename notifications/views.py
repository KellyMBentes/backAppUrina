from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NotificationSerializer, OptionSerializer
from .models import Notification, Option
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

notification_response = openapi.Response('OK', NotificationSerializer)
option_response = openapi.Response('OK', OptionSerializer)


@swagger_auto_schema(method='get',
    responses={
        '200': notification_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET', ])
def get_notification(request, pk):
    data = {}
    try:
        notification = Notification.objects.get(id=pk)
    except Notification.DoesNotExist:
        data['error'] = 'Object Not Found.'
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NotificationSerializer(notification)
        return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='get',
    responses={
        '200': option_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET', ])
def get_option(request, pk):
    data = {}
    try:
        option = Option.objects.get(id=pk)
    except Option.DoesNotExist:
        data['error'] = 'Object Not Found.'
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OptionSerializer(option)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
    data = {}

    if request.method == 'POST':
        serializer = NotificationSerializer(notification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data['error'] = serializer.errors
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='put', request_body=NotificationSerializer,
    responses={
        '202': 'Accepted',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@swagger_auto_schema(method='delete', request_body=NotificationSerializer,
    responses={
        '200': 'OK',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['PUT', 'DELETE'])
def update_delete_notification(request, pk):
    data = {}
    try:
        notification = Notification.objects.get(id=pk)
    except Notification.DoesNotExist:
        data['error'] = "Object Not Found."
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = NotificationSerializer(notification, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        data['error'] = serializer.errors
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        operation = notification.delete()
        data = {}
        if operation:
            data['response'] = "Delete successful"
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data['error'] = "Delete failed"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=OptionSerializer,
                     responses={
                         '201': 'Created',
                         '400': 'Bad Request',
                         '401': 'Unauthorized',
                     })
@api_view(['POST', ])
def create_option(request, pk):
    data = {}
    try:
        notification = Notification.objects.get(id=pk)
    except Notification.DoesNotExist:
        data['error'] = "Object Not Found."
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    option = Option(notification=notification)

    if request.method == 'POST':
        serializer = OptionSerializer(option, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='put', request_body=OptionSerializer,
    responses={
        '202': 'Accepted',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@swagger_auto_schema(method='delete',
    responses={
        '200': 'OK',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['PUT', 'DELETE'])
def update_delete_option(request, pk):
    data = {}
    try:
        option = Option.objects.get(id=pk)
    except Option.DoesNotExist:
        data['error'] = 'Object Not Found.'
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OptionSerializer(option, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        data['error'] = serializer.errors
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        operation = option.delete()
        data = {}
        if operation:
            data['response'] = "Delete successful"
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data['error'] = "Delete failed"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
