from django_filters.rest_framework import filters, FilterSet
from django.contrib.gis.geos import Point
from api.models import ServiceArea


class ServiceAreaFilter(FilterSet):
    def filter_queryset(self, queryset):
        coordinates = self.request.query_params.get("coordinates")
        if coordinates:
            try:
                point = Point(list(map(float, coordinates.split(","))))
                return queryset.filter(area__contains=point)
            except ValueError:
                pass
        return super().filter_queryset(queryset)
