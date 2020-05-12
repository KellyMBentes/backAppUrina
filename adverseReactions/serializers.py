from rest_framework import serializers
from .models import AdverseReaction


class AdverseReactionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = AdverseReaction
        fields = ['id', 'user','medicine', 'date', 'skin_rash', 'skin_swelling', 'blood_pressure_fall',
                  'consciousness_loss', 'difficult_of_breathing', 'comment']
