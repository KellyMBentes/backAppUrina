"""appUrinaDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from users.models import CustomUser

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
    path('apiDocumentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('apiDocumentationReDoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('apiDocumentation/', schema_view),
    path('api/user/', include('users.urls', 'api_users')),
    path('api/personalData/', include('personalData.urls', 'api_personalData')),
    path('api/notification/', include('notifications.urls', 'api_notifications')),
    path('api/liquidIntake/', include('liquidIntake.urls', 'api_liquidIntake')),
    path('api/peeDiary/', include('peeDiary.urls', 'api_peeDiary')),
    path('api/question/', include('questions.urls', 'api_questions')),
    path('api/news/', include('news.urls', 'api_news')),
    path('api/score/', include('score.urls', 'api_score'))

    # REST FRAMEWORK
    # path('api/', include('api.urls', 'api')),
]
