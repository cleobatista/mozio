from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """Provider viewset for CRUD operations on provider model"""

    model = Provider
    pagination_class = PageNumberPagination
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """Provider viewset for CRUD operations on provider model"""

    model = ServiceArea
    pagination_class = PageNumberPagination
    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()
