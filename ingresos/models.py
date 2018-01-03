from django.db import models
from django.core.validators import RegexValidator

class Client(models.Model):
    client = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="El número de teléfono debe ingresarse en el formato: '7751234567'. Hasta 10 dígitos permitidos.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)

    def __str__(self):
        return self.cliente


class Sale (models.Model):
    PAYMENTS = (('TC', 'Tarjeta Credito'),
                ('Efectivo', 'Efectivo'),
                ('TD', 'Tarjeta Debito'))
    created = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, related_name="cli", on_delete=models.CASCADE)
    units = models.PositiveIntegerField(default=1)
    kg_total = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    payment = models.CharField(max_length=100, choices=PAYMENTS, )
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "Venta no. {}".format(self.id)


class Product(models.Model):
    name = models.CharField(max_length= 140)
    category = models.CharField(max_length = 140)
    uprice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

#Prueba

class SaleItem(models.Model):
    order = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    #price = models.DecimalField(max_digits=10, decimal_places=2)
    weigth = models.DecimalField(max_digits=10, decimal_places=2)
    animal_ref = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.product.uprice*self.weigth
