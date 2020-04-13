from rest_framework import serializers

from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = Notification
        fields = ['id', 'option', 'user']