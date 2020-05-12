from django.urls import path
from questions import views


app_name = 'questionForm'

urlpatterns = [
    path('', views.create_questionForm, name="create"),
    path('<int:pk>', views.read_questionForm, name="read"),
    path('<int:pk>/', views.update_delete_questionForm, name="edit-or-delete"),
    path('<int:pk>/option/', views.create_option, name="create-option"),
    path('option/<int:pk>', views.read_option, name="read-option"),
    path('option/<int:pk>/', views.update_delete_option, name="edit-or-delete-option"),
]
