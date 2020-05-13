from . import views
from django.urls import path

app_name = 'chat'

urlpatterns = [
    path('/messages/<int:receiver>', views.message_list, name='message-detail'),  # For GET request.
    # URL form : "/api/messages/"
    path('/messages/', views.message_post, name='message-list'),   # For POST
]
