from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LiquidIntakeSerializer
from .models import LiquidIntake


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
