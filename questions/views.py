from rest_framework import status
from rest_framework.response import Response

from .serializers import QuestionFormSerializer
from rest_framework.decorators import api_view
from .models import QuestionForm


@api_view(['POST', ])
def create_questionForm(request):
    user = request.user

    questionForm = QuestionForm(user=user)

    if request.method == 'POST':
        serializer = QuestionFormSerializer(questionForm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
