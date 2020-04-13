from django.urls import path
from users import views
from .views import obtain_auth_token

app_name = 'users'

urlpatterns = [
    path('register', views.registration_view, name='register'),
    path('login', obtain_auth_token, name="login")
]