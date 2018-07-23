from django.db import models
from django.core.validators import RegexValidator


class CuentaBanco(models.Model):
    cuenta = models.CharField(max_length=16, blank=True, null=True, unique=True)
    banco=models.CharField(max_length=140, blank=True, null=True)
    clabe=models.CharField(max_length=140, blank=True, null=True, unique=True)

    def __unicode__(self):
        return self.cuenta

    class Meta:
        ordering = ["-id"]


class Client(models.Model):
    client = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    rfc = models.CharField(max_length=20, default="", unique=True)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="El número de teléfono debe ingresarse en el formato: '7751234567'. Hasta 10 dígitos permitidos.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True, null=True)
    direct_contact = models.BooleanField(default=False)
    name_contact = models.CharField(max_length=140, blank=True)
    phone_contact = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    comments_contact = models.CharField(max_length=140, blank=True, null=True)
    credit = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.client

    class Meta:
        ordering = ["-id"]


class BusinessLine(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
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
    address = models.TextField(blank=True, null=True)
    #direct_contact = models.BooleanField(default=False)
    #name_contact = models.CharField(max_length=140, blank=True)
    #phone_contact = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    #comments_contact = models.CharField(max_length=140, blank=True)

    def __unicode__(self):
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
    client = models.ForeignKey(Client, related_name="sales", on_delete=models.PROTECT, blank=True, null=True)
    empresa = models.ForeignKey(Company, related_name="incomes", on_delete=models.SET_NULL, blank=True, null=True)
    sale_check = models.BooleanField(default=False)
    no_scheck = models.CharField(max_length=140, blank=True, null=True)
    paid = models.BooleanField(default=False)
    business_line = models.ForeignKey(BusinessLine, related_name="sales", on_delete=models.PROTECT, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    receivable = models.ForeignKey(CuentaBanco, related_name='sales', on_delete=models.PROTECT, blank=True, null=True)
    concepto = models.CharField(max_length=140, blank=True, null=True)
    sale_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unidad = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    is_sale = models.BooleanField(default=False)

    class Meta:
        ordering = ["-id"]

    def __unicode__(self):
        return "Venta no. {}".format(self.id)

#Prueba

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.PROTECT)
    #product = models.ForeignKey(Product, related_name='sale_items', on_delete=models.PROTECT, default="")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weigth = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    animal_ref = models.CharField(max_length=100, default="")

    def __unicode__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.product.uprice*self.weigth
