from django.urls import path
from peeDiary import views

app_name = 'peeDiary'

urlpatterns = [
    path('create', views.create_peeDiary, name="create"),
    path('<int:id>/', views.read_peeDiary, name="detail"),
    path('', views.get_all_peeDiary, name="get-all-pee-diary"),
    path('edit/<id>', views.update_peeDiary, name="edit"),
    path('delete/<id>', views.delete_peeDiary, name="delete"),

]
