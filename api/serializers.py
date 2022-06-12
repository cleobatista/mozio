from dataclasses import fields
from rest_framework import serializers
from .models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"
        read_only_fields = ("id")

class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = "__all__"
        read_only_fields = ("id")