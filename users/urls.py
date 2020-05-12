from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.registration_view, name='register'),
    path('login/', views.decorated_login_view, name="login"),
    path('change-password/', views.ChangePassword.as_view(), name="changePassword"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('reset-password/<email>', views.passwordReset, name="resetPassword"),
    path('change-password-reset/<uidb64>/<token>/', views.changePasswordReset, name="changePasswordReset"),
]
