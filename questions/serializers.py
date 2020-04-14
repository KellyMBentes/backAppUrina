from rest_framework import serializers
from .models import QuestionForm


class QuestionFormSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = QuestionForm
        fields = ['id', 'user', 'option', 'title', 'slider', 'type']
