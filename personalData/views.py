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

    personal = PersonalData(user=user)
    if request.method == 'POST':
        serializer = PersonalDataSerializer(personal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='put', request_body=PersonalDataSerializer,
    responses={
        '200': 'OK',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['PUT', ])
def update_personalData(request, id):
    try:
        personal = PersonalData.objects.get(id=id)
    except PersonalData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PersonalDataSerializer(personal, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get',
    responses={
        '200': user_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET', ])
def read_personalData(request, id):
    try:
        personal = PersonalData.objects.get(id=id)
    except PersonalData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonalDataSerializer(personal)
        return Response(serializer.data)


@swagger_auto_schema(method='delete',
    responses={
        '200': 'OK',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['DELETE', ])
def delete_personalData(request, id):
    try:
        personal = PersonalData.objects.get(id=id)
    except PersonalData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = personal.delete()
        data = {}
        if operation:
            data["success"] = "Delete successful"
        else:
            data["failure"] = "Delete unsuccesful"
        return Response(data=data)


@swagger_auto_schema(method='post', request_body=PhoneSerializer,
    responses={
        '201': 'Created',
        '400': 'Bad Request',
        '401': 'Unauthorized',
    })
@api_view(['POST', ])
def create_phone(request, id):
    personal = PersonalData.objects.get(id=id)
    phone = Phone(personalData=personal)

    if request.method == 'POST':
        serializer = PhoneSerializer(phone, data=request.data)
        if serializer.is_valid():
            print(personal)
            serializer.save()
            personal.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(method='get',
    responses={
        '200': phone_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET', ])
def read_phone(request, id):
    try:
        phone = Phone.objects.get(id=id)
    except Phone.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhoneSerializer(phone)
        return Response(serializer.data)


@swagger_auto_schema(method='put', request_body=PhoneSerializer,
    responses={
        '200': 'OK',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['PUT', ])
def update_phone(request, id):
    try:
        phone = Phone.objects.get(id=id)
    except Phone.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PhoneSerializer(phone, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='delete',
    responses={
        '200': 'OK',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['DELETE', ])
def delete_phone(request, id):
    try:
        phone = Phone.objects.get(id=id)
    except Phone.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = phone.delete()
        data = {}
        if operation:
            data["success"] = "Delete successful"
        else:
            data["failure"] = "Delete unsuccesful"
        return Response(data=data)



