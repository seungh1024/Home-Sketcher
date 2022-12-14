"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg       import openapi

# swagger
schema_view = get_schema_view(
    openapi.Info(
        title="HomeStecher-Project",
        default_version='1.1.1',
        description="HomeStecher",
        terms_of_service="",
        contact=openapi.Contact(email=""), # 부가정보
        license=openapi.License(name="mit"),     # 부가정보
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


api_urlpatterns = ([
    # swagger
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    
    # app url
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('auths/', include('auths.urls', namespace="auths")),
    path('interests/', include('interests.urls', namespace="auths")),
    path('furnitures/',include('furnitures.urls',namespace="furnitures")),
    path('interests/', include('interests.urls', namespace="interests")),
    path('likes/', include('likes.urls', namespace="likes")),
    path('recommendations/', include('recommendations.urls', namespace="recommendations")),
    path('threedimensions/', include('threedimensions.urls', namespace="threedimensions")),
],'api/v1')

urlpatterns=[
    path('api/v1/',include(api_urlpatterns))
]
