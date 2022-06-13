from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer
from .filters import ServiceAreaFilter


class ProviderViewSet(viewsets.ModelViewSet):
    """Provider viewset for CRUD operations on provider model"""

    model = Provider
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    ordering = ["id"]


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """Provider viewset for CRUD operations on provider model"""

    model = ServiceArea
    filterset_class = ServiceAreaFilter
    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()
    ordering = ["id"]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValueError as error:
            return Response(
                data={"detail": error.args[0]}, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except ValueError as error:
            return Response(
                data={"detail": error.args[0]}, status=status.HTTP_400_BAD_REQUEST
            )
