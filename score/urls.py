from django.urls import path
from score import views


app_name = 'score'

urlpatterns = [
    path('<int:pk>', views.get_score, name="detail"),
    path('create', views.create_score, name="create"),
]
