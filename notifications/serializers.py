from rest_framework import serializers
from .models import Notification, Option


class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'user', 'isSelectedAll', 'isPriority']


class OptionSerializer(serializers.ModelSerializer):
    notification = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Option
        fields = ['id', 'notification', 'isSelected', 'isPriority', 'text', 'type']
