import random
import string

from coreapi.compat import force_bytes
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.contrib.sites.shortcuts import get_current_site
from django.core import mail
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .tokens import account_activation_token
from .serializers import RegistrationSerializer, MyAuthTokenSerializer
from rest_framework.authtoken import views as auth_views
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from .serializers import MyAuthTokenSerializer, data1Register, dataLogin, ChangePasswordSerializer, \
    ChangePasswordSerializer2
from appUrinaDjango import settings
from .models import CustomUser
from django.contrib.auth.models import User


#########################################
# Visualização da serialização do login

# Obtem o token no momento do login passando o email e a senha
@permission_classes([AllowAny])
class MyAuthToken(auth_views.ObtainAuthToken):
    serializer_class = MyAuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="Valid email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )


obtain_auth_token = MyAuthToken.as_view()

serializerData = openapi.Response('OK', dataLogin)

decorated_login_view = \
    swagger_auto_schema(
        method='post', request_body=MyAuthTokenSerializer,
        responses={
            '200': serializerData,
            '201': 'Created',
            '400': 'Bad Request',
            '401': 'Unauthorized',
        }
    )(obtain_auth_token)

#########################################
# Visualização da serialização do registro

serializerData2 = openapi.Response('OK', data1Register)


@swagger_auto_schema(method='post', request_body=RegistrationSerializer,
                     responses={
                         '200': serializerData2,
                         '201': 'Created',
                         '400': 'Bad Request',
                     })
@api_view(['POST', ])
@permission_classes([AllowAny])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            user.save()
            sendEmail(request, user, 'Activate your account! Team Plethora', 'active_email.html',0)
            data['response'] = 'Succesfully registered a new user, but not yet activated.'
            data['email'] = user.email

        else:
            data = serializer.errors
        return Response(data=data)


# Função para realizar a ativação do usuário após clicar no link com uid e token, fornecido por email
@api_view(('GET',))
@permission_classes([AllowAny])
def activate(request, uidb64, token):
    data = {}
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        data['response'] = 'Succesfully activated user.'
        data['email'] = user.email
    else:
        data['response'] = 'User activation failed.'
    return Response(data=data)


# Função que recebe alguns parâmetros e os repassa para o envio de um email
def sendEmail(request, user, subject, template, *args):

    mail_subject = subject
    from_email = settings.EMAIL_HOST_USER
    html_content = render_to_string(template, {
        'user': user,
        'domain': request.get_host(),
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "password": args[0]
    })
    text_content = strip_tags(html_content)
    to_email = user.email
    mail.send_mail(mail_subject, text_content, from_email, [to_email], html_message=html_content, fail_silently=True)


# Endpoint para alteração de senha do usuário logado
class ChangePassword(APIView):

    def get_object(self, queryset=None):
        return self.request.user

    @swagger_auto_schema(method='put', request_body=ChangePasswordSerializer,
                         responses={
                             '200': 'OK',
                             '400': 'Bad Request',
                             '401': 'Unauthorized',
                         })
    @action(detail=True, methods=['put'])
    def put(self, request, *args, **kwargs):
        data = {}
        print(request.user)
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            # Checa a senha antiga
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                data['response'] = 'Wrong password'
                return Response(data=data,
                                status=status.HTTP_400_BAD_REQUEST)
            # Seta a nova senha fornecida pelo usuário
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            user = request.user
            sendEmail(request, user, 'Your password was changed.', 'change_password.html', 0)
            data['response'] = 'Password updated succesfully.'
            return Response(data=data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


@api_view(('GET',))
@permission_classes([AllowAny])
def passwordReset(request, email):
    data = {}
    try:
        user = CustomUser.objects.get(email=email)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    print(user, user.id)
    if user is not None:
            password = randomString()
            print(password)
            user.set_password(password)
            user.save()
            print(user.check_password(password))
            sendEmail(request, user, 'Reset your password.', 'user_reset_password.html', password)
            data['response'] = 'A email of reset was sent.'
    else:
        data['response'] = 'Unidentify email.'
    return Response(data=data)

@swagger_auto_schema(method='put', request_body=ChangePasswordSerializer,
                         responses={
                             '200': 'OK',
                             '400': 'Bad Request',
                             '401': 'Unauthorized',
                         })
@api_view(('PUT',))
@permission_classes([AllowAny])
def changePasswordReset(request, uidb64, token):
    data = {}
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = CustomUser.objects.get(pk=uid)
        print(user)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
            # Checa a senha antiga
        old_password = request.data.get("old_password")
        if not user.check_password(old_password):
            data['response'] = 'Wrong password'
            return Response(data=data,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
        # Seta a nova senha fornecida pelo usuário
            user.set_password(request.data.get("new_password"))
            user.save()
            sendEmail(request, user, 'Your password was changed.', 'change_password.html',0)
            data['response'] = 'Password updated succesfully.'
            return Response(data=data)

    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
