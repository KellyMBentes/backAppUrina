from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import MedicineSerializer
from .models import Medicine


@api_view(['GET', ])
@permission_classes([AllowAny])
def read_med(request):
    data = {}
    try:
        med = Medicine.objects.all()
    except Medicine.DoesNotExist:
        data['error'] = "Object not found"
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MedicineSerializer(med, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST', ])
@permission_classes([AllowAny])
def create_med(request):
    if request.method == 'POST':
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
