from django.urls import path

from liquidIntake import views
from .views import update_liquidIntake

app_name = 'liquidIntake'

urlpatterns = [
    path('create', views.create_liquidIntake, name="create"),
    path('<id>/', views.read_liquidIntake, name="detail"),
    path('edit/<id>', update_liquidIntake, name="edit"),
    path('delete/<id>', views.delete_liquidIntake, name="delete")
]
