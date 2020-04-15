from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import QuestionFormSerializer, OptionSerializer
from .models import QuestionForm, Option


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


@api_view(['GET'])
def read_questionForm(request, pk):
    try:
        form = QuestionForm.objects.get(id=pk)
    except QuestionForm.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionFormSerializer(form)
        return Response(serializer.data)


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


@api_view(['POST', ])
def create_option(request, pk):

    option = Option(formId=pk)

    if request.method == 'POST':
        serializer = OptionSerializer(option, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def read_option(request, pk):
    try:
        option = Option.objects.get(id=pk)
    except Option.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OptionSerializer(option)
        return Response(serializer.data)


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
            data["success"] = "Update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
