from django.urls import path
from questions import views


app_name = 'questionForm'

urlpatterns = [
    path('create', views.create_questionForm, name="create")
]
