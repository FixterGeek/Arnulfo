from django.db import models

class Corral(models.Model):
    MONTHS = (('Enero', 'Enero'),
              ('Febrero', 'Febrero'),
              ('Marzo', 'Marzo'),
              ('Abril', 'Abril'),
              ('Mayo', 'Mayo'),
              ('Junio', 'Junio'),
              ('Julio', 'Julio'),
              ('Agosto', 'Agosto'),
              ('Septiembre', 'Septiembre'),
              ('Octubre', 'Octubre'),
              ('Noviembre', 'Noviembre'),
              ('Diciembre', 'Diciembre'),
              )
    fecha_generacion = models.DateTimeField(auto_now_add=False, db_index=True)
    no_corral = models.PositiveIntegerField(default=0)
    comentarios = models.TextField()
    status = models.BooleanField(default=False)
    numero_semana = models.PositiveIntegerField(default=0)
    ano = models.PositiveIntegerField(default=2010)
    numero_serial = models.CharField(max_length=100)
    mes = models.CharField(max_length=100, choices=MONTHS, )
    cuarto = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Corral no. {}".format(self.id)

class Lote(models.Model):
    name = models.CharField(max_length=130)
    status = models.BooleanField(default=False)
    corral = models.ForeignKey(Corral, related_name='lotes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Alimento(models.Model):
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Alimentación no. {}".format(self.id)

class Animal(models.Model):
    MONTHS = (('Enero','Enero'),
              ('Febrero', 'Febrero'),
              ('Marzo', 'Marzo'),
              ('Abril', 'Abril'),
              ('Mayo', 'Mayo'),
              ('Junio', 'Junio'),
              ('Julio', 'Julio'),
              ('Agosto', 'Agosto'),
              ('Septiembre', 'Septiembre'),
              ('Octubre', 'Octubre'),
              ('Noviembre', 'Noviembre'),
              ('Diciembre', 'Diciembre'),
              )
    arete_siniga = models.CharField(max_length=30)
    arete_rancho = models.CharField(max_length=30)
    fecha_entrada = models.DateTimeField(auto_now_add=False, db_index=True)
    fecha_registro = models.DateTimeField(auto_now_add=True, db_index=True)
    peso_entrada = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    costo_kilo = models.DecimalField(max_digits=10, decimal_places=2)
    raza = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    comentarios = models.TextField()
    owner = models.CharField(max_length=150)
    lote_corral = models.ForeignKey(Lote, related_name='animals', on_delete=models.CASCADE)
    alimento = models.ForeignKey(Alimento, related_name='animals', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    numero_semana = models.PositiveIntegerField(default=0)
    ano = models.PositiveIntegerField(default=2010)
    mes = models.CharField(max_length=100, choices=MONTHS, )
    cuarto = models.CharField(max_length=100)
    costo_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    fierro_original = models.ImageField(upload_to='fierrosO/')
    fierro_nuevo = models.ImageField(upload_to='fierrosN/')
    ref_factura_original = models.CharField(max_length=100)

    def __str__(self):
        return self.arete_rancho



