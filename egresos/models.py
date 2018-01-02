from django.db import models


class Provider(models.Model):
    provider = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    email = models.CharField(max_length=140)
    phone = models.IntegerField()

    def __str__(self):
        return self.provider


class Purchase (models.Model):
    provider = models.ForeignKey(Provider, related_name="provid", on_delete=models.CASCADE)
    units = models.IntegerField()
    uprice = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "Compra no. {}".format(self.id)


class Product(models.Model):
    name = models.CharField(max_length= 140)
    category = models.CharField(max_length = 140)
    units = models.IntegerField()

    def __str__(self):
        return self.name
