from drf_yasg import openapi
from rest_framework import serializers
from .models import PersonalData, Phone
from django.contrib.auth.models import User

class PersonalDataSerializer(serializers.ModelSerializer):

    email = serializers.SerializerMethodField('get_email_from_user')

    phone = serializers.SerializerMethodField('get_number_from_phone')

    class Meta:
        model = PersonalData
        depth = 1
        fields = ['id', 'name', 'email', 'birthDate', 'gender', 'phone', 'cpf', 'rg', 'cep', 'addressNumber', 'addressComplement',
                  'addressStreet', 'addressCity', 'addressDistrict', 'addressFederalState', 'healthEnsurance', 'healthEnsuranceCompany',
                  'healthEnsuranceDescription', 'hasHealthData', 'hasPersonalData', 'hasPrescription', 'hasQrMedication']

    def get_email_from_user(self, personal):
        email = personal.user.email
        return email

    def get_number_from_phone(self, personal):
        number = personal.phone.number
        return number

class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        depth = 1
        fields = ['id', 'number']