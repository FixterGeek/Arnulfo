from django.db import models

# Create your models here.
class Vacuna(models.Model):
    vaccine = models.CharField(max_length=100)
    typeofv = models.CharField(max_length=100)
    dose = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unity = models.CharField(max_length=100, blank=True, null=True)
    content = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    concentration = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        return self.vaccine
