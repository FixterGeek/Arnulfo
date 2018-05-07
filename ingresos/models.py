from django.db import models
from django.core.validators import RegexValidator
from egresos.models import Product

class Client(models.Model):
    client = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    rfc = models.CharField(max_length=20, default="", unique=True)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="El número de teléfono debe ingresarse en el formato: '7751234567'. Hasta 10 dígitos permitidos.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    direct_contact = models.BooleanField(default=False)
    name_contact = models.CharField(max_length=140, blank=True)
    phone_contact = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    comments_contact = models.CharField(max_length=140, blank=True)

    def __str__(self):
        return self.client

    class Meta:
        ordering = ["-id"]


class BusinessLine(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]

class Company(models.Model):
    LINES = (('Cerdos', 'Cerdos'),
             ('Ganado', 'Ganado'),
             ('Granos', 'Granos'),
             ('Planta de alimentos', 'Planta de alimentos'),
             ('Campo', 'Campo')
             )
    company = models.CharField(max_length=140)
    line_comp = models.ManyToManyField(BusinessLine, related_name='companies')
    rfc_comp = models.CharField(max_length=20, default="", unique=True)
    email_comp = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="El número de teléfono debe ingresarse en el formato: '7751234567'. Hasta 10 dígitos permitidos.")
    phone_compa = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    #direct_contact = models.BooleanField(default=False)
    #name_contact = models.CharField(max_length=140, blank=True)
    #phone_contact = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    #comments_contact = models.CharField(max_length=140, blank=True)

    def __str__(self):
        return self.company

    class Meta:
        ordering = ["-id"]




class Sale (models.Model):
    LINES = (('Cerdos', 'Cerdos'),
             ('Ganado', 'Ganado'),
             ('Granos', 'Granos'),
             ('Planta de alimentos', 'Planta de alimentos'),
             ('Campo', 'Campo')
             )
    created = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, related_name="sales", on_delete=models.CASCADE, blank=True, null=True)
    sale_check = models.BooleanField(default=False)
    no_scheck = models.CharField(max_length=140, blank=True, null=True)
    paid = models.BooleanField(default=False)
    business_line = models.CharField(max_length=100, choices=LINES, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # receivable = a que cuenta se ligará

    def __str__(self):
        return "Venta no. {}".format(self.id)

#Prueba

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='sale_items', on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weigth = models.DecimalField(max_digits=10, decimal_places=2)
    animal_ref = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.product.uprice*self.weigth
