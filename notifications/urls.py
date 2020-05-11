from django.urls import path
from notifications import views


app_name = 'notification'

urlpatterns = [
    path('<int:pk>', views.get_notification, name="detail"),
    path('', views.create_notification, name="create"),
    path('<int:pk>/', views.update_delete_notification, name="edit-or-delete"),
    path('option/<int:pk>', views.get_option, name="detail-option"),
    path('<int:notification_id>/option/', views.create_option, name="create-option"),
    path('option/<int:pk>/', views.update_delete_option, name="edit-or-delete-option"),
]

