from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LiquidIntakeSerializer,BeverageSerializer
from .models import LiquidIntake,Beverage
import requests
import json

liquid_intake_response = openapi.Response('OK', LiquidIntakeSerializer)


@swagger_auto_schema(method='post', request_body=LiquidIntakeSerializer,
    responses={
        '201': 'Created',
        '400': 'Bad Request',
        '401': 'Unauthorized',
    })
@api_view(['POST', ])
def create_liquidIntake(request,pk):
    user = request.user
    beverage = Beverage(id=pk)
    liquidIntake = LiquidIntake(user=user, beverage=beverage)
    if request.method == 'POST':
        serializer = LiquidIntakeSerializer(liquidIntake, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get',
    responses={
        '200': liquid_intake_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET', ])
def read_liquidIntake(request, id):
    try:
        liquid = LiquidIntake.objects.get(id=id)
    except LiquidIntake.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LiquidIntakeSerializer(liquid)
        r = requests.get('https://jsonplaceholder.typicode.com/users')
        r = json.loads(r.content)
        return Response(r)


@swagger_auto_schema(method='put', request_body=LiquidIntakeSerializer,
    responses={
        '200': 'OK',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['PUT', ])
def update_liquidIntake(request, id):
    try:
        liquid = LiquidIntake.objects.get(id=id)
    except LiquidIntake.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = LiquidIntakeSerializer(liquid, data=request.data)
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
def delete_liquidIntake(request, id):
    try:
        liquid = LiquidIntake.objects.get(id=id)
    except LiquidIntake.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = liquid.delete()
        data = {}
        if operation:
            data["success"] = "Delete successful"
        else:
            data["failure"] = "Delete unsuccesful"
        return Response(data=data)



@swagger_auto_schema(method='post', request_body=BeverageSerializer,
    responses={
        '201': 'Created',
        '400': 'Bad Request',
        '401': 'Unauthorized',
    })

@api_view(['POST', ])
def create_beverage(request):

    beverage =Beverage()
    if request.method == 'POST':
        serializer = BeverageSerializer(beverage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get',
    responses={
        '200': liquid_intake_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET', ])
def read_beverage(request, id):
    try:
        beverage = Beverage.objects.get(id=id)
    except Beverage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BeverageSerializer(beverage)
        return Response(serializer.data)


@swagger_auto_schema(method='put', request_body=BeverageSerializer,
    responses={
        '200': 'OK',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['PUT', ])
def update_beverage(request, id):
    try:
        beverage = Beverage.objects.get(id=id)
    except Beverage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BeverageSerializer(beverage, data=request.data)
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
def delete_beverage(request, id):
    try:
        beverage = Beverage.objects.get(id=id)
    except Beverage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = beverage.delete()
        data = {}
        if operation:
            data["success"] = "Delete successful"
        else:
            data["failure"] = "Delete unsuccesful"
        return Response(data=data)
