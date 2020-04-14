from django.urls import path
from notifications import views


app_name = 'notification'

urlpatterns = [
    path('create', views.create_notification, name="create")
]
