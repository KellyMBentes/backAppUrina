from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg import openapi
from chat.models import Message
from chat.serializers import MessageSerializer

chat_response = openapi.Response('OK', MessageSerializer)


@swagger_auto_schema(method='get', responses={
        '200': chat_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
    })
@api_view(['GET', ])
def message_list(request, receiver=None):
    content = {}
    if request.method == 'GET':
        user = request.user
        offset = request.query_params.get('offset', None)
        limit = request.query_params.get('limit', None)
        data = {}

        if offset is not None and limit is not None:
            offset = int(offset)
            limit = int(limit)
            if offset >= limit:
                data['error'] = "offset param must be less than limit param."
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
            else:
                messages = Message.objects.filter(sender_id=user, receiver_id=receiver).order_by("-timestamp") | \
                           Message.objects.filter(sender_id=receiver, receiver_id=user).order_by("-timestamp")
                content = messages.filter()[offset:limit]
        elif offset is None and limit is None:
            data['error'] = "limit param is required."
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        elif offset is None and limit is not None:
            limit = int(limit)
            messages = Message.objects.filter(sender_id=user, receiver_id=receiver).order_by("-timestamp") | \
                       Message.objects.filter(sender_id=receiver, receiver_id=user).order_by("-timestamp")
            content = messages.filter()[:limit]
        elif offset is not None and limit is None:
            data['error'] = "offset param requires a limit param."
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'GET':
            serializer = MessageSerializer(content, many=True, context={'request': request})
            if serializer.data.__len__() == 0:
                data['error'] = "could not retrieve any message"
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='post', request_body=MessageSerializer,
                     responses={
                         '201': 'Created',
                         '400': 'Bad Request',
                         '401': 'Unauthorized',
                     })
@api_view(['POST', ])
def message_post(request):
    if request.method == 'POST':
        user = request.user
        data = {}
        message = Message(sender=user)
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data['error'] = serializer.errors
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
