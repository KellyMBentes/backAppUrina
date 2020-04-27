from rest_framework import serializers
from .models import LiquidIntake, Beverage


class BeverageSerializer(serializers.ModelSerializer):
    liquid = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Beverage
        fields = ['id', 'liquid', 'name']


class LiquidIntakeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    beverage = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = LiquidIntake
        fields = ['id', 'user', 'createdDate', 'beverage', 'volume']
