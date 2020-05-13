from django.urls import path
from medicines import views

app_name = 'medicines'

urlpatterns = [
    path('/', views.create_med, name="create"),
    path('', views.read_med, name="detail"),
]