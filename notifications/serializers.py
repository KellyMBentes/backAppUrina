from rest_framework import serializers
from .models import Notification, Option


class NotificationSerializer(serializers.ModelSerializer):
    userId = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'userId', 'isSelectedAll', 'isPriority']


class OptionSerializer(serializers.ModelSerializer):
    notificationId = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Option
        fields = ['id', 'notificationId', 'isSelected', 'isPriority', 'text', 'type']
