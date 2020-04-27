from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ScoreSerializer
from .models import Score


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


@api_view(['GET'])
def get_score(request):
    user = request.user
    try:
        score = Score.objects.get(user=user)
    except Score.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ScoreSerializer(score)
        return Response(serializer.data)
