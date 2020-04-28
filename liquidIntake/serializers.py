from rest_framework import serializers
from .models import LiquidIntake


class LiquidIntakeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = LiquidIntake
        fields = ['id', 'user', 'createdDate', 'beverage', 'volume']
