from rest_framework import serializers
from .models import QuestionForm, Option


class QuestionOptionSerializer(serializers.ModelSerializer):
    form = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Option
        fields = ['id', 'form', 'text']


class QuestionFormSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = QuestionForm
        fields = ['id', 'user', 'title', 'slider', 'type']
