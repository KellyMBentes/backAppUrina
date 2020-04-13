from django.urls import path

from .views import create_notification


app_name = 'notification'

urlpatterns = [
    path('create/', create_notification, name="create")
]