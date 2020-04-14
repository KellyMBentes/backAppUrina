from django.urls import path

from liquidIntake import views

app_name = 'liquidIntake'

urlpatterns = [
    path('create', views.create_liquidIntake, name="create")
]
