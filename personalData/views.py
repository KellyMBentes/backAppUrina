from django.shortcuts import render
from drf_yasg import openapi
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PersonalData, Phone
from .serializers import PersonalDataSerializer, PhoneSerializer
from drf_yasg.utils import swagger_auto_schema

user_response = openapi.Response('OK', PersonalDataSerializer)
phone_response = openapi.Response('OK', PhoneSerializer)


@swagger_auto_schema(method='post', request_body=PersonalDataSerializer,
    responses={
        '201': 'Created',
        '400': 'Bad Request',
        '401': 'Unauthorized',
    })
@api_view(['POST', ])
def create_personalData(request):
    user = request.user
    data = {}
    try:
        personal = PersonalData.objects.get(user=user)
        data['error'] = "Duplicate key error collection: user can't have more than one personal data"
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    except PersonalData.DoesNotExist:
        personal = PersonalData(user=user)

    if request.method == 'POST':
        serializer = PersonalDataSerializer(personal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data['error'] = serializer.errors
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get',
    responses={
        '200': user_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET', ])
def read_personalData(request, id):
    data = {}
    try:
        personal = PersonalData.objects.get(id=id)
    except PersonalData.DoesNotExist:
        data['error'] = "Object Not Found."
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonalDataSerializer(personal)
        return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='put', request_body=PersonalDataSerializer,
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
def update_delete_personalData(request, id):
    data = {}
    try:
        personal = PersonalData.objects.get(id=id)
    except PersonalData.DoesNotExist:
        data['error'] = "Object Not Found."
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PersonalDataSerializer(personal, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        data['error'] = serializer.errors
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        operation = personal.delete()
        data = {}
        if operation:
            data['response'] = "Delete successful"
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data['error'] = "Delete failed"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=PhoneSerializer,
    responses={
        '201': 'Created',
        '400': 'Bad Request',
        '401': 'Unauthorized',
    })
@api_view(['POST', ])
def create_phone(request, id):
    data = {}
    try:
        personal = PersonalData.objects.get(id=id)
    except PersonalData.DoesNotExist:
        data['error'] = "Object Not Found."
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    phone = Phone(personalData=personal)

    if request.method == 'POST':
        serializer = PhoneSerializer(phone, data=request.data)
        if serializer.is_valid():
            serializer.save()
            personal.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data['error'] = serializer.errors
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get',
    responses={
        '200': phone_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET', ])
def read_phone(request, id):
    data = {}
    try:
        phone = Phone.objects.get(id=id)
    except Phone.DoesNotExist:
        data['error'] = "Object not found"
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhoneSerializer(phone)
        return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='put', request_body=PhoneSerializer,
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
def update_delete_phone(request, id):
    data = {}
    try:
        phone = Phone.objects.get(id=id)
    except Phone.DoesNotExist:
        data['error'] = "Object Not Found."
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PhoneSerializer(phone, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        data['error'] = serializer.errors
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        operation = phone.delete()
        data = {}
        if operation:
            data['response'] = "Delete successful"
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data['error'] = "Delete failed"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)





