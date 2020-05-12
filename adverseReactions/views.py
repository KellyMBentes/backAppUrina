from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AdverseReactionSerializer
from .models import AdverseReaction
from medicines.models import Medicine

adverse_reaction_response = openapi.Response('OK', AdverseReactionSerializer)


@swagger_auto_schema(method='post', request_body=AdverseReaction,
                     responses={
                         '201': 'Created',
                         '400': 'Bad Request',
                         '401': 'Unauthorized',
                     })
@api_view(['POST', ])
def create_adverseReaction(request):
    user = request.user
    data = {}
    try:
        medicine = Medicine.objects.get(id=request.data["medicine"])
    except Medicine.DoesNotExist:
        data["error"] = "Object not found"
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    adverseReaction = AdverseReaction(user=user, medicine=medicine)

    if request.method == 'POST':
        serializer = AdverseReactionSerializer(adverseReaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get',
                     responses={
                         '200': adverse_reaction_response,
                         '400': 'Bad Request',
                         '401': 'Unauthorized',
                         '404': 'Not Found',
                     })
@api_view(['GET', ])
def read_adverseReaction(request, id):
    data = {}
    try:
        adverseReaction = AdverseReaction.objects.get(id=id)
    except adverseReaction.DoesNotExist:
        data['error'] = "Object not found"
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdverseReactionSerializer(adverseReaction)
        return Response(serializer.data)


@swagger_auto_schema(method='put', request_body=AdverseReactionSerializer,
                     responses={
                         '202': 'Accepted',
                         '400': 'Bad Request',
                         '401': 'Unauthorized',
                         '404': 'Not Found',
                     })
@swagger_auto_schema(method='delete', request_body=AdverseReactionSerializer,
                     responses={
                         '200': 'OK',
                         '401': 'Unauthorized',
                         '404': 'Not Found',
                     })
@api_view(['PUT', 'DELETE'])
def update_delete_adverseReaction(request, id):
    try:
        adverseReaction = AdverseReaction.objects.get(id=id)
    except AdverseReaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AdverseReactionSerializer(adverseReaction, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'Update successful'
            return Response(data=data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        operation = adverseReaction.delete()
        data = {}
        if operation:
            data["response"] = "Delete successful"
        else:
            data["response"] = "Delete failed"
        return Response(data=data)
