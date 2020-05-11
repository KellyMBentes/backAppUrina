from django.urls import path
from peeDiary import views

app_name = 'peeDiary'

urlpatterns = [
    path('', views.create_list_peeDiary, name="create"),
    path('<int:pk>', views.read_peeDiary, name="detail"),
    path('<int:pk>/', views.update_delete_peeDiary, name="edit-or-delete"),
]
