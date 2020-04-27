from rest_framework import serializers
from .models import Score


class ScoreSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Score
        fields = ['id', 'user', 'level', 'exp', 'consecutiveDays']
