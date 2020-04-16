from rest_framework import serializers
from .models import PeeDiary


class PeeDiarySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = PeeDiary
        fields = ['id', 'user', 'createdDate', 'peeVolume', 'effortToUrinate', 'hasLost',
                  'isDoingPhysicalActivity', 'referenceVolume']
