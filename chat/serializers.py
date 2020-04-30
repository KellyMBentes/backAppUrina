from rest_framework import serializers
from chat.models import Message
from users.models import CustomUser


class MessageSerializer(serializers.ModelSerializer):
    """For Serializing Message"""
    sender =  serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    receiver = serializers.SlugRelatedField(many=False, slug_field='id', queryset=CustomUser.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
