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
