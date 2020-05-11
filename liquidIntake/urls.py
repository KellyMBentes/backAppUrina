from django.urls import path

from liquidIntake import views

app_name = 'liquidIntake'

urlpatterns = [
    path('', views.create_liquidIntake, name="create"),
    path('<int:id>', views.read_liquidIntake, name="detail"),
    path('<int:id>/', views.update_delete_liquidIntake, name="edit-or-delete"),
]
