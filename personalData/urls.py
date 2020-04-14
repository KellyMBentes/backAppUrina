from django.urls import path
from .views import read_personalData, update_personalData, delete_personalData, create_personalData, create_phone, read_phone, update_phone, delete_phone

app_name = "personalData"

urlpatterns = [
    path('create', create_personalData, name='create'),
    path('<id>/', read_personalData, name='detail'),
    path('edit/<id>', update_personalData, name='edit'),
    path('delete/<id>', delete_personalData, name='delete'),

    path('phone/create', create_phone, name='createPhone'),
    path('phone/<id>/', read_phone, name='detailPhone'),
    path('phone/edit/<id>', update_phone, name='editPhone'),
    path('phone/delete/<id>', delete_phone, name='deletePhone'),

]