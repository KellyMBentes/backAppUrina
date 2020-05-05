from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ScoreSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Score
import os

score_response = openapi.Response('OK', ScoreSerializer)


@swagger_auto_schema(method='post', request_body=ScoreSerializer,
    responses={
        '201': 'Created',
        '400': 'Bad Request',
        '401': 'Unauthorized',
    })
@api_view(['POST'])
def create_score(request):
    user = request.user
    data = {}
    try:
        score = Score.objects.get(user=user)
        data['errors'] = 'duplicate key error collection: user must be unique'
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    except Score.DoesNotExist:
        score = Score(user=user)

        if request.method == "POST":
            serializer = ScoreSerializer(score, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get',
    responses={
        '200': score_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET'])
def get_score(request):
    user = request.user

    try:
        score = Score.objects.get(user=user)
    except Score.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # update_score(user, 120)
        serializer = ScoreSerializer(score)
        return Response(serializer.data)


def update_score(user, expGain, multiplier=1):
    success = False

    try:
        score = Score.objects.get(user=user)
    except Score.DoesNotExist:
        return success

    file = open(os.path.join(settings.BASE_DIR, 'scoreSettings'), "r")
    lines = []
    for line in file:
        line = line.rstrip()
        lines.append(line)
    file.close()

    if multiplier > 3:
        multiplier = 3

    score.exp += expGain*multiplier

    if (0 < score.level < 6) and len(lines) != 0:
        line = lines[score.level].split()
        expRequired = int(line[2])

        if score.exp >= expRequired:
            score.level += 1

        score.save()
        success = True

    return success
