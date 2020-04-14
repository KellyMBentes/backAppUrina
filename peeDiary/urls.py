from django.urls import path
from peeDiary import views

app_name = 'peeDiary'

urlpatterns = [
    path('create', views.create_peeDiary, name="create")
]
