from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import MedicineSerializer
from .models import  Medicine
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET', ])
@permission_classes([AllowAny])
def read_med(request,):
    try:
        med = Medicine.objects.all()
    except Medicine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MedicineSerializer(med, many=True)
        return Response(serializer.data)

@api_view(['POST', ])
@permission_classes([AllowAny])
def create_med(request):
    if request.method == 'POST':
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)