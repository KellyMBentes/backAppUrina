from rest_framework.decorators import api_view

from chat.models import Message
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from chat.serializers import MessageSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@api_view(['GET', ])
def message_list(request,receiver=None):
    if request.method == 'GET':
        user = request.user
        print(user)
        messages = Message.objects.filter(sender_id=user, receiver_id=receiver) | Message.objects.filter(sender_id=receiver, receiver_id=user)

        serializer = MessageSerializer(messages, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)


@api_view(['POST', ])
def message_post(request, sender=None, receiver=None):
    if request.method == 'POST':
        user = request.user
        data = JSONParser().parse(request)
        message = Message(sender=user)
        serializer = MessageSerializer(message, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
