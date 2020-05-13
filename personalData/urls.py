from django.urls import path
from personalData import views

app_name = "personalData"

urlpatterns = [
    path('/', views.create_personalData, name='create'),
    path('/<int:id>', views.read_personalData, name='detail'),
    path('/<int:id>/', views.update_delete_personalData, name='edit-or-delete'),

    path('/<int:id>/phone/', views.create_phone, name='create-phone'),
    path('/phone/<int:id>', views.read_phone, name='detail-phone'),
    path('/phone/<int:id>/', views.update_delete_phone, name='edit-delete-phone'),
]
