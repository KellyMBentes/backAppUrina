from django.urls import path
from peeDiary import views

app_name = 'peeDiary'

urlpatterns = [
    path('create', views.create_peeDiary, name="create"),
    path('<int:pk>/', views.read_peeDiary, name="detail"),
    path('', views.list_peeDiary, name="list-peeDiary"),
    path('edit/<int:pk>', views.update_peeDiary, name="edit"),
    path('delete/<int:pk>', views.delete_peeDiary, name="delete"),
]
