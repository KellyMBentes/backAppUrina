from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import QuestionFormSerializer, QuestionOptionSerializer
from .models import QuestionForm, Option

questionForm_response = openapi.Response('OK', QuestionFormSerializer)
option_response = openapi.Response('OK', QuestionOptionSerializer)


@swagger_auto_schema(method='post', request_body=QuestionFormSerializer,
    responses={
        '201': 'Created',
        '400': 'Bad Request',
        '401': 'Unauthorized',
    })
@api_view(['POST', ])
def create_questionForm(request):
    user = request.user
    try:
        question= QuestionForm.objects.get(user=user)
        data = {}
        data['response'] = "User cannot have more than one question form"
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    except QuestionForm.DoesNotExist:
        questionForm = QuestionForm(user=user)

        if request.method == 'POST':
            serializer = QuestionFormSerializer(questionForm, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get',
    responses={
        '200': questionForm_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET'])
def read_questionForm(request, pk):
    try:
        form = QuestionForm.objects.get(id=pk)
    except QuestionForm.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionFormSerializer(form)
        return Response(serializer.data)


@swagger_auto_schema(method='put', request_body=QuestionFormSerializer,
    responses={
        '200': 'Success',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['PUT', ])
def update_questionForm(request, pk):
    try:
        form = QuestionForm.objects.get(id=pk)
    except QuestionForm.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = QuestionFormSerializer(form, data=request.data)
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
def delete_questionForm(request, pk):
    try:
        form = QuestionForm.objects.get(id=pk)
    except QuestionForm.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = form.delete()
        data = {}
        if operation:
            data["success"] = "Delete successful"
        else:
            data["failure"] = "Delete unsuccesful"
        return Response(data=data)


@swagger_auto_schema(method='post', request_body=QuestionOptionSerializer,
    responses={
        '201': 'Created',
        '400': 'Bad Request',
        '401': 'Unauthorized',
    })
@api_view(['POST', ])
def create_option(request, pk):
    questionForm= QuestionForm.objects.get(id=pk)
    option = Option(formId=questionForm)

    if request.method == 'POST':
        serializer = QuestionOptionSerializer(option, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get',
    responses={
        '200': option_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET'])
def read_option(request, pk):
    try:
        option = Option.objects.get(id=pk)
    except Option.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionOptionSerializer(option)
        return Response(serializer.data)


@swagger_auto_schema(method='put', request_body=QuestionOptionSerializer,
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
        serializer = QuestionOptionSerializer(option, data=request.data)
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
def delete_option(request, pk):
    try:
        option = Option.objects.get(id=pk)
    except Option.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = option.delete()
        data = {}
        if operation:
            data["success"] = "Delete successful"
        else:
            data["failure"] = "Delete unsuccesful"
        return Response(data=data)
