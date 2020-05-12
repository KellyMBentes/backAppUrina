from django.urls import path

from images import views

app_name = 'image'

urlpatterns = [
    path('', views.create_image, name="create"),
    path('<int:id>', views.read_image, name="detail"),
    path('<int:id>/', views.update_delete_image, name="edit-or-delete"),
]