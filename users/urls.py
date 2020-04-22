from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register', views.registration_view, name='register'),
    path('login', views.decorated_login_view, name="login"),
    path('changePassword', views.ChangePassword, name="changePassword"),
]