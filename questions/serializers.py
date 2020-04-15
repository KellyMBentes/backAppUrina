from rest_framework import serializers
from .models import QuestionForm, Option


class OptionSerializer(serializers.ModelSerializer):
    formId = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Option
        fields = ['id', 'formId', 'text']


class QuestionFormSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = QuestionForm
        fields = ['id', 'user', 'title', 'slider', 'type']
