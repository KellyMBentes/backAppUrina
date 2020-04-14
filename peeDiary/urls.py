from django.urls import path
from peeDiary import views

app_name = 'peeDiary'

urlpatterns = [
    path('create', views.create_peeDiary, name="create"),
    path('<id>/', views.read_peeDiary, name="detail"),
    path('edit/<id>', views.update_peeDiary, name="edit"),
    path('delete/<id>', views.delete_peeDiary, name="delete")
]
