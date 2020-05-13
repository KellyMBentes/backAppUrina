from django.urls import path
from score import views


app_name = 'score'

urlpatterns = [
    path('/', views.create_score, name="create"),
    path('/<int:pk>', views.get_score, name="detail"),
]
