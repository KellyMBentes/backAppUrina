from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'user', 'firebaseKey']
