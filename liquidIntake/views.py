from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LiquidIntakeSerializer
from .models import LiquidIntake

liquid_intake_response = openapi.Response('response description', LiquidIntakeSerializer)


@swagger_auto_schema(method='post', request_body=LiquidIntakeSerializer,
    responses={
        '201': 'Created',
        '400': 'Bad Request',
        '401': 'Unauthorized',
    })
@api_view(['POST', ])
def create_liquidIntake(request):
    user = request.user

    liquidIntake = LiquidIntake(user=user)

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
        return Response(serializer.data)


@swagger_auto_schema(method='put', request_body=LiquidIntakeSerializer,
    responses={
        '200': 'Success',
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
        '200': 'Success',
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
