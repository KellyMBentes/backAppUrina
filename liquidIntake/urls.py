from django.urls import path

from liquidIntake import views

app_name = 'liquidIntake'

urlpatterns = [
    path('create/', views.create_liquidIntake, name="create"),
    path('<id>/', views.read_liquidIntake, name="detail"),
    path('edit/<id>', views.update_liquidIntake, name="edit"),
    path('delete/<id>', views.delete_liquidIntake, name="delete"),

]
