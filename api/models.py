from django.db import models
from django.contrib.gis.db import models as gmodels


class Provider(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=128)
    language = models.CharField(max_length=128)
    currency = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name


class ServiceArea(models.Model):
    name = models.CharField(max_length=128)
    provider = models.ForeignKey(
        Provider, related_name="provider", on_delete=models.CASCADE
    )
    price = models.FloatField()
    area = gmodels.PolygonField()

    def __str__(self) -> str:
        return f"{self.provider.name} - {self.name}"
