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


@api_view(['GET', ])
def get_all_peeDiary(request, offset=-1, limit=-1, peeVolume=-1):
    try:
        user = request.user
        data = {}
        offset = request.query_params.get('offset', None)
        limit = request.query_params.get('limit', None)
        peeVolume = request.query_params.get('peeVolume', None)
        if offset is not None and limit is not None and peeVolume is not None:
            offset = int(offset)
            limit = int(limit)
            peeVolume = int(peeVolume)
            pee = PeeDiary.objects.all().filter(user=user, peeVolume=peeVolume)[offset:limit]
        elif offset is not None and limit is not None:
            offset = int(offset)
            limit = int(limit)
            pee = PeeDiary.objects.all().filter(user=user)[offset:limit]
        elif offset is None and limit is not None and peeVolume is not None:
            limit = int(limit)
            peeVolume = int(peeVolume)
            pee = PeeDiary.objects.all().filter(user=user, peeVolume=peeVolume)[:limit]
        elif offset is None and limit is None and peeVolume is not None:
            peeVolume = int(peeVolume)
            pee = PeeDiary.objects.all().filter(user=user, peeVolume=peeVolume)
            print("enteri aqui")
        elif offset is not None and limit is None:
           data['error'] = "offset param requires a limit param."
           return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        elif offset is None and limit is not None:
            limit = int(limit)
            pee = PeeDiary.objects.all().filter(user=user)[:limit]
        else:
            pee = PeeDiary.objects.filter(user=user)
            print(pee)
    except PeeDiary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        print("#",pee)
        serializer = PeeDiarySerializer(pee, many=True)
        print("@",serializer.data)
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
