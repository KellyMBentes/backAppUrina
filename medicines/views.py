from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from .serializers import MedicineSerializer
from .models import Medicine


@swagger_auto_schema(method='get',
    responses={
        '200': 'OK',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
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


@swagger_auto_schema(method='post', request_body=MedicineSerializer,
    responses={
        '201': 'Created',
        '400': 'Bad Request',
        '401': 'Unauthorized',
    })
@api_view(['POST', ])
@permission_classes([AllowAny])
def create_med(request):
    data = {}
    if request.method == 'POST':
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data['error'] = serializer.errors
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
