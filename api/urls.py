from django.urls import path, include
from rest_framework import routers
from .views import ProviderViewSet, ServiceAreaViewSet

router = routers.DefaultRouter()
router.register('provider', ProviderViewSet)
router.register('service_area', ServiceAreaViewSet)

urlpatterns = path('', include(routers.urls))