from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import RegistrationSerializer, MyAuthTokenSerializer
from rest_framework.authtoken import views as auth_views
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from .serializers import MyAuthTokenSerializer, data1Register, dataLogin, ChangePasswordSerializer
from .models import CustomUser
from django.contrib.auth.models import User


#########################################
#Visualização da serialização do login

#Obtem o token no momento do login passando o email e a senha
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
#Visualização da serialização do registro

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
            token = Token.objects.get(user=user).key
            data['response'] = 'Succesfully registered a new user.'
            data['email'] = user.email
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data=data)


#Endpoint para alteração de senha
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
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                data['response'] = 'Wrong password'
                return Response(data=data,
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            data['response'] = 'Password updated successfully'
            return Response(data=data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
