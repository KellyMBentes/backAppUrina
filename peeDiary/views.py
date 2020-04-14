from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PeeDiarySerializer
from .models import PeeDiary


@api_view(['POST', ])
def create_peeDiary(request):
    user = request.user

    peeDiary = PeeDiary(user=user)

    if request.method == 'POST':
        serializer = PeeDiarySerializer(peeDiary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def read_peeDiary(request, id):
    try:
        pee = PeeDiary.objects.get(id=id)
    except PeeDiary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PeeDiarySerializer(pee)
        return Response(serializer.data)


@api_view(['PUT', ])
def update_peeDiary(request, id):
    try:
        pee = PeeDiary.objects.get(id=id)
    except PeeDiary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PeeDiarySerializer(pee, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def delete_peeDiary(request, id):
    try:
        pee = PeeDiary.objects.get(id=id)
    except PeeDiary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = pee.delete()
        data = {}
        if operation:
            data["success"] = "Delete successful"
        else:
            data["failure"] = "Delete unsuccesful"
        return Response(data=data)