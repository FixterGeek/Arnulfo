from django.db import models
from egresos.models import Provider

# Create your models here.
class Insumo(models.Model):
    name = models.CharField(max_length=100)
    provider = models.ForeignKey(Provider, related_name='insumos', on_delete=models.CASCADE, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # unit = models.CharField(max_length=140)

    def __str__(self):
        return self.name

class Formula(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    insumo = models.ForeignKey(Insumo, related_name='items', on_delete=models.CASCADE, blank=True)
    formula = models.ForeignKey(Formula, related_name='items', on_delete=models.CASCADE, blank=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.insumo.name
