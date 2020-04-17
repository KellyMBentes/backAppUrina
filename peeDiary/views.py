from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PeeDiarySerializer
from .models import PeeDiary

pee_diary_response = openapi.Response('OK', PeeDiarySerializer)
pee_diary_list_response = openapi.Response('OK', PeeDiarySerializer(many=True))

offset = openapi.Parameter('offset', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
limit = openapi.Parameter('limit', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
peeVolume = openapi.Parameter('peeVolume', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)


@swagger_auto_schema(method='post', request_body=PeeDiarySerializer,
    responses={
        '201': 'Created',
        '400': 'Bad Request',
        '401': 'Unauthorized',
    })
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


@swagger_auto_schema(method='get',
    responses={
        '200': pee_diary_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET', ])
def read_peeDiary(request, pk):
    try:
        pee = PeeDiary.objects.get(id=pk)
    except PeeDiary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PeeDiarySerializer(pee)
        return Response(serializer.data)


@swagger_auto_schema(method='get',
    manual_parameters=[offset, limit, peeVolume],
    responses={
        '200': pee_diary_list_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET', ])
def list_peeDiary(request):
    try:
        user = request.user
        data = {}
        offset = request.query_params.get('offset', None)
        limit = request.query_params.get('limit', None)
        peeVolume = request.query_params.get('peeVolume', None)
        if offset is not None and limit is not None and peeVolume is not None:
            offset = int(offset)
            limit = int(limit)
            peeVolume = float(peeVolume)
            pee = PeeDiary.objects.filter(user=user, peeVolume=peeVolume)[offset:limit]
        elif offset is not None and limit is not None:
            offset = int(offset)
            limit = int(limit)
            pee = PeeDiary.objects.filter(user=user)[offset:limit]
        elif offset is None and limit is not None and peeVolume is not None:
            limit = int(limit)
            peeVolume = float(peeVolume)
            pee = PeeDiary.objects.filter(user=user, peeVolume=peeVolume)[:limit]
        elif offset is None and limit is None and peeVolume is not None:
            peeVolume = float(peeVolume)
            pee = PeeDiary.objects.filter(user=user, peeVolume=peeVolume)
            # pee = PeeDiary.objects.filter(user=user, peeVolume__gte=peeVolume)  # greater than equal
            # pee = PeeDiary.objects.filter(user=user, peeVolume__lte=peeVolume)  # less than equal
        elif offset is not None and limit is None:
            data['error'] = "offset param requires a limit param."
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        elif offset is None and limit is not None:
            limit = int(limit)
            pee = PeeDiary.objects.filter(user=user)[:limit]
        else:
            pee = PeeDiary.objects.filter(user=user)
    except PeeDiary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PeeDiarySerializer(pee, many=True)
        return Response(serializer.data)


@swagger_auto_schema(method='put', request_body=PeeDiarySerializer,
    responses={
        '200': 'Success',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['PUT', ])
def update_peeDiary(request, pk):
    try:
        pee = PeeDiary.objects.get(id=pk)
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


@swagger_auto_schema(method='delete',
    responses={
        '200': 'Success',
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['DELETE', ])
def delete_peeDiary(request, pk):
    try:
        pee = PeeDiary.objects.get(id=pk)
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
