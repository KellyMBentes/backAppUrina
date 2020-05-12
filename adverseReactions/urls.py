from django.urls import path
from adverseReactions import views

app_name = 'liquidIntake'

urlpatterns = [
    path('', views.create_adverseReaction, name="create"),
    path('<int:id>', views.read_adverseReaction, name="detail"),
    path('<int:id>/', views.update_delete_adverseReaction, name="edit-or-delete"),


]