from django.urls import path

from liquidIntake import views

app_name = 'liquidIntake'

urlpatterns = [
    path('create/<int:pk>', views.create_liquidIntake, name="create"),
    path('beverage/create', views.create_beverage, name="create-option"),
    path('<id>/', views.read_liquidIntake, name="detail"),
    path('beverage/<int:pk>', views.read_beverage, name="detail-beverage"),
    path('edit/<id>', views.update_liquidIntake, name="edit"),
    path('edit/beverage/<id>', views.update_beverage, name="edit-beverage"),
    path('delete/<id>', views.delete_liquidIntake, name="delete"),
    path('delete/beverage/<id>', views.delete_beverage, name="delete-beverage")

]
