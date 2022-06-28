"""drf3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# register here
# router.register('dogapiviewset', DogViewSet, basename= 'dogviewset')
router.register('dogmodelviewset', DogModelViewSet, basename='dogmodelviewset')
# router.register('dogreadonlymodelviewset', DogReadOnlyViewSet, basename='dogreadonlymodelviewset')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest.urls')),
    path('api', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='apiview')),
]
