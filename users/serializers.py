from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import action

from .models import CustomUser

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = CustomUser(
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords must match'})

        user.set_password(password)
        user.save()

        return user

# Serializa e valida o email e senha, e se ok gera um token
@method_decorator(name='validate', decorator=swagger_auto_schema(
    operation_description="description from swagger_auto_schema via method_decorator"
))
class MyAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password",),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    @swagger_auto_schema(method='post', operation_description="POST /articles/{id}/image/")
    @action(detail=False, methods=['post'])
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

class register_response(object):
    def __init__(self):
        self.response = 'Succesfully registered a new user.'
        self.email = 'string'
        self.token = 'string'


class registerSerializer(serializers.Serializer):
    response = serializers.CharField(max_length=55, default='Succesfully registered a new user.')
    email = serializers.CharField(max_length=55)
    token = serializers.CharField(max_length=55)

class login_response(object):
    def __init__(self):
        self.token = 'string'


class loginSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=55)


data1Register = registerSerializer(register_response)
dataLogin = loginSerializer(login_response)