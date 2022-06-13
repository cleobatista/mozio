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


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """Provider viewset for CRUD operations on provider model"""

    model = ServiceArea
    filterset_class = ServiceAreaFilter
    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        except ValueError as error:
            return Response(
                data={"detail": error.args[0]}, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop("partial", False)
            instance = self.get_object()
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial
            )
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, "_prefetched_objects_cache", None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        except ValueError as error:
            return Response(
                data={"detail": error.args[0]}, status=status.HTTP_400_BAD_REQUEST
            )
