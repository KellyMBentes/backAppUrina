from django.urls import path
from questions import views


app_name = 'questionForm'

urlpatterns = [
    path('create', views.create_questionForm, name="create"),
    path('create/option/<int:pk>', views.create_option, name="create-option"),
    path('<int:pk>', views.read_questionForm, name="read"),
    path('option/<int:pk>',views.read_option, name="read-option"),
    path('update/<int:pk>',views.update_questionForm,name="update"),
    path('update/option/<int:pk>', views.update_option, name="update-option"),
    path('delete/<int:pk>', views.delete_questionForm,name="delete"),
    path('delete/option/<int:pk>', views.delete_option,name="delete-option")
]
