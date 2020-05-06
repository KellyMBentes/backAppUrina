from django.contrib.auth.password_validation import validate_password
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import action
from django.contrib.auth.models import User
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
class MyAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password",),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

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


#Cria um model para ser mostrado no swagger como formato da resposta para o POST de registro
class registerSerializer(serializers.Serializer):
    response = serializers.CharField(max_length=55, default='Succesfully registered a new user.')
    email = serializers.CharField(max_length=55)
    token = serializers.CharField(max_length=55)


#Cria uma classe somente para preencher o model anterior registerSerializer
class register_response(object):
    def __init__(self):
        self.response = 'Succesfully registered a new user.'
        self.email = 'string'
        self.token = 'string'


#Cria um model para ser mostrado no swagger como formato de resposta para o POST de login
class loginSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=55)


#Cria uma classe somente para preencher o model anterior loginSerializer
class login_response(object):
    def __init__(self):
        self.token = 'string'


data1Register = registerSerializer(register_response)
dataLogin = loginSerializer(login_response)


#Serializa para alterar a senha do usuário
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class ChangePasswordSerializer2(serializers.Serializer):


    def validate_new_password(self, value):
        validate_password(value)
        return value
