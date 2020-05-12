from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Urina APP API",
      default_version='v1',
      description="API Django REST - Urina App",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/documentation-redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/documentation/', schema_view),
    path('api/user', include('users.urls', 'api_users')),
    path('api/personal-data', include('personalData.urls', 'api_personalData')),
    path('api/notification', include('notifications.urls', 'api_notifications')),
    path('api/liquid-intake', include('liquidIntake.urls', 'api_liquidIntake')),
    path('api/pee-diary', include('peeDiary.urls', 'api_peeDiary')),
    path('api/question', include('questions.urls', 'api_questions')),
    path('api/news', include('news.urls', 'api_news')),
    path('api/score', include('score.urls', 'api_score')),
    path('api/chat', include('chat.urls', 'api_chat')),
    path('api/medicines/', include('medicines.urls', 'api_medicines')),
    path('api/adverseReactions/', include('adverseReactions.urls', 'api_adverseReactions'))
]
