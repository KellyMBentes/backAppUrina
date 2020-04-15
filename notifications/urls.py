from django.urls import path
from notifications import views


app_name = 'notification'

urlpatterns = [
    path('<int:pk>', views.get_notification, name="get"),
    path('create', views.create_notification, name="create"),
    path('update/<int:pk>', views.update_notification, name="update"),
    path('delete/<int:pk>', views.delete_notification, name="delete"),
    path('option/<int:pk>', views.get_option, name="get"),
    path('option/create', views.create_option, name="create"),
    path('option/update/<int:pk>', views.update_option, name="update"),
    path('option/delete/<int:pk>', views.delete_option, name="delete")
]

