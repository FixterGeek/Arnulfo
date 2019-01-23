

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingresos', '0001_initial'),
        ('vacunas', '0001_initial'),
        ('planta_alimentos', '0001_initial'),

    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arete_siniga', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('arete_rancho', models.CharField(blank=True, max_length=30, null=True)),
                ('fecha_entrada', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('peso_entrada', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('costo_kilo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('color', models.CharField(blank=True, max_length=150, null=True)),
                ('owner', models.CharField(blank=True, max_length=150, null=True)),
                ('tipo_animal', models.CharField(blank=True, choices=[('becerro', 'becerro'), ('toro', 'toro'), ('vaca', 'vaca'), ('vaquilla', 'vaquilla')], max_length=100, null=True)),
                ('status', models.BooleanField(default=True)),
                ('costo_inicial', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fierro_original', models.ImageField(blank=True, null=True, upload_to='fierrosO/')),
                ('fierro_nuevo', models.ImageField(blank=True, null=True, upload_to='fierrosN/')),
                ('merma', models.CharField(blank=True, max_length=100, null=True)),
                ('days_in_ranch', models.CharField(blank=True, default='0', max_length=100)),
                ('kg_hechos', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('conversion', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('rendimiento', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('costo_por_dia', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ganacia_diaria_promedio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('otromas', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animals', to='ingresos.Company')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Corral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_generacion', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('no_corral', models.CharField(max_length=100, unique=True)),
                ('comentarios', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('numero_serial', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factura', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='FierroN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='fierros/n')),
            ],
        ),
        migrations.CreateModel(
            name='FierroO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='fierros/o')),
            ],
        ),
        migrations.CreateModel(
            name='GastoAnimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(blank=True, null=True)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unity', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo', models.CharField(blank=True, choices=[('Alimento', 'Alimento'), ('Vacuna', 'Vacuna')], max_length=100, null=True)),
                ('insumo', models.CharField(blank=True, max_length=100, null=True)),
                ('insumo_q', models.IntegerField(blank=True, null=True)),
                ('insumo_cost', models.IntegerField(blank=True, null=True)),
                ('animal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='aliments', to='ganado.Animal')),
                ('formula', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='gastos_animal', to='planta_alimentos.Formula')),
                ('vacuna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='gastos_animal', to='vacunas.Vacuna')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('corral', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lotes', to='ganado.Corral')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Peso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=10)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pesadas', to='ganado.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SaleNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('kilograms', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('carro', models.CharField(blank=True, max_length=100, null=True)),
                ('chofer', models.CharField(blank=True, max_length=100, null=True)),
                ('flete', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sale_notes', to='ingresos.Client')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='fierroN',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animals', to='ganado.FierroN'),
        ),
        migrations.AddField(
            model_name='animal',
            name='fierroO',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animals', to='ganado.FierroO'),
        ),
        migrations.AddField(
            model_name='animal',
            name='lote',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animals', to='ganado.Lote'),
        ),
        migrations.AddField(
            model_name='animal',
            name='raza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animals', to='ganado.Raza'),
        ),
        migrations.AddField(
            model_name='animal',
            name='ref_factura_original',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animals', to='ganado.Factura'),
        ),
        migrations.AddField(
            model_name='animal',
            name='sale_note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animals', to='ganado.SaleNote'),
        ),
    ]
