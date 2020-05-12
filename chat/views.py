from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view

from chat.models import Message
from drf_yasg import openapi
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from chat.serializers import MessageSerializer
from django.views.decorators.csrf import csrf_exempt

chat_response = openapi.Response('OK', MessageSerializer)


@swagger_auto_schema(method='get', responses={
        '200': chat_response,
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '404': 'Not Found',
        '405': 'Method Not Allowed',
    })
@api_view(['GET', ])
def message_list(request, receiver=None):
    global content
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
                return JsonResponse(data=data, status=status.HTTP_400_BAD_REQUEST)
            else:
                messages = Message.objects.filter(sender_id=user, receiver_id=receiver).order_by("-timestamp") | Message.objects.filter(
                    sender_id=receiver, receiver_id=user).order_by("-timestamp")

                content = messages.filter()[offset:limit]
        elif offset is None and limit is not None :
            limit = int(limit)
            messages = Message.objects.filter(sender_id=user, receiver_id=receiver).order_by(
                "-timestamp") | Message.objects.filter(
                sender_id=receiver, receiver_id=user).order_by("-timestamp")
            content = messages.filter()[:limit]
        elif offset is not None and limit is None:
            data['error'] = "offset param requires a limit param."
            return JsonResponse(data=data, status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'GET':
            serializer = MessageSerializer(content, many=True, context={'request': request})
            if serializer.data.__len__() == 0:
                data["error"] = "could not retrieve any message"
                return JsonResponse(data=data, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse(serializer.data, safe=False)



@swagger_auto_schema(method='post', request_body=MessageSerializer,
                     responses={
                         '201': 'Created',
                         '400': 'Bad Request',
                         '401': 'Unauthorized',
                         '405': 'Method Not Allowed',
                     })
@api_view(['POST', ])
def message_post(request, sender=None, receiver=None):
    if request.method == 'POST':
        user = request.user
        data = JSONParser().parse(request)
        message = Message(sender=user)
        serializer = MessageSerializer(message, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
