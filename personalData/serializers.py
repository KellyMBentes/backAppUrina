from rest_framework import serializers
from .models import PersonalData, Phone
from django.contrib.auth.models import User

class PersonalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        depth = 1
        fields = ['id', 'name', 'birthDate', 'gender', 'cpf', 'rg', 'addressNumber', 'addressComplement',
                  'healthEnsurance', 'healthEnsuranceCompany', 'healthEnsuranceDescription', 'hasHealthData',
                  'hasPersonalData', 'hasPrescription', 'hasQrMedication']

class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        depth = 1
        fields = ['id', 'number']