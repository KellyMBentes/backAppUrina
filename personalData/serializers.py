from drf_yasg import openapi
from rest_framework import serializers
from .models import PersonalData, Phone


class PersonalDataSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    email = serializers.SerializerMethodField('get_email_from_user')

    class Meta:
        model = PersonalData
        depth = 1
        fields = ['id', 'user', 'name', 'email', 'birthDate', 'gender', 'cpf', 'rg', 'cep', 'addressNumber',
                  'addressComplement', 'addressStreet', 'addressCity', 'addressDistrict', 'addressFederalState',
                  'healthEnsurance', 'healthEnsuranceCompany', 'healthEnsuranceDescription', 'hasHealthData',
                  'hasPersonalData', 'hasPrescription', 'hasQrMedication', 'schooling', 'civilStatus', 'birthPlace',
                  'occupation', 'ethnicity', 'familyIncome']

    def get_email_from_user(self, personal):
        email = personal.user.email
        return email


class PhoneSerializer(serializers.ModelSerializer):
    personalData = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Phone
        depth = 1
        fields = ['id', 'personalData', 'number']
