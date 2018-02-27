from django.db import models


class Raza(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.name

class Corral(models.Model):
    
    fecha_generacion = models.DateTimeField(auto_now_add=True, db_index=True)
    no_corral = models.PositiveIntegerField(unique=True)
    comentarios = models.TextField()
    status = models.BooleanField(default=True)
    numero_serial = models.CharField(max_length=100, unique=True)
    # numero_semana = models.PositiveIntegerField(default=0)
    # ano = models.PositiveIntegerField(default=2010)
    
    # mes = models.CharField(max_length=100, choices=MONTHS, )
    # cuarto = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Corral no. {}".format(self.no_corral)

class Lote(models.Model):
    name = models.CharField(max_length=130, unique=True)
    status = models.BooleanField(default=True)
    corral = models.OneToOneField(Corral, related_name='lotes', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name



class Animal(models.Model):
   
    TIPOA = (('becerro', 'becerro'),
            ('toro', 'toro'),
            ('vaca', 'vaca'),
            ('vaquilla', 'vaquilla')
            )
    arete_siniga = models.CharField(max_length=30, blank=True, null=True)
    arete_rancho = models.CharField(max_length=30, blank=True, null=True, unique=True)
    fecha_entrada = models.DateTimeField(auto_now_add=False, db_index=True, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True, db_index=True, blank=True, null=True)
    peso_entrada = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    costo_kilo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    raza = models.ForeignKey(Raza, related_name='animals', on_delete=models.SET_NULL, blank=True, null=True)
    color = models.CharField(max_length=150, blank=True, null=True)
    #comentarios = models.TextField()
    owner = models.CharField(max_length=150, blank=True, null=True)
    lote = models.ForeignKey(Lote, related_name='animals', on_delete=models.SET_NULL, blank=True, null=True)
    tipo_animal = models.CharField(max_length=100, choices=TIPOA, blank=True, null=True)
    
    status = models.BooleanField(default=True)
    costo_inicial = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fierro_original = models.ImageField(upload_to='fierrosO/', blank=True, null=True)
    fierro_nuevo = models.ImageField(upload_to='fierrosN/', blank=True, null=True)
    ref_factura_original = models.CharField(max_length=100, blank=True, null=True)
    merma = models.CharField(max_length=100, blank=True, null=True)

    # numero_semana = models.PositiveIntegerField(default=0, blank=True, null=True)
    # ano = models.PositiveIntegerField(default=2010, blank=True, null=True)
    # mes = models.CharField(max_length=100, choices=MONTHS, blank=True, null=True)
    # cuarto = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.arete_rancho


class GastoAnimal(models.Model):
    TIPO=(
    ('Alimento','Alimento'),
    ('Vacuna', 'Vacuna'))
    created = models.DateField(auto_now_add=True, blank=True, null=True)
    animal = models.ForeignKey(Animal, related_name='aliments', on_delete=models.PROTECT, null=True, blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
    tipo = models.CharField(max_length=100, choices=TIPO, blank=True, null=True)
    


    def __str__(self):
        return "Gasto no. {}, {} ".format(self.id, self.tipo)

class Peso(models.Model):
  created = models.DateField(auto_now_add=True)
  peso = models.DecimalField(max_digits=10, decimal_places=2)
  animal = models.ForeignKey(Animal, related_name='pesadas', on_delete=models.PROTECT)

  def __str__(self):
    return "Animal {} Weigths {} kg".format(self.animal.id, self.peso)





