

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingresos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_factura', models.CharField(max_length=140)),
                ('descripcion', models.CharField(max_length=140)),
                ('fecha_creacion', models.DateField(blank=True, db_index=True, null=True)),
                ('costo_final', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('linea_compras', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='compras', to='ingresos.BusinessLine')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='GastoGanado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concepto', models.CharField(max_length=140)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField(auto_now_add=True, db_index=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('category', models.CharField(max_length=40)),
                ('uprice', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=140)),
                ('address', models.CharField(max_length=140)),
                ('rfc', models.CharField(default='', max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="El número de teléfono debe ingresarse en el formato: '7751234567'. Hasta 10 dígitos permitidos.", regex='^\\+?1?\\d{9,10}$')])),
                ('direct_contact', models.BooleanField(default=False)),
                ('name_contact', models.CharField(blank=True, max_length=140)),
                ('phone_contact', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="El número de teléfono debe ingresarse en el formato: '7751234567'. Hasta 10 dígitos permitidos.", regex='^\\+?1?\\d{9,10}$')])),
                ('comments_contact', models.CharField(blank=True, max_length=140)),
                ('credit', models.CharField(blank=True, max_length=140)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('purchase_check', models.BooleanField(default=False)),
                ('no_check', models.CharField(blank=True, max_length=140, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('type', models.CharField(blank=True, choices=[('Gasto', 'Gasto'), ('Costo', 'Costo')], max_length=100, null=True)),
                ('concepto_purchase', models.CharField(blank=True, max_length=140, null=True)),
                ('compra_check', models.BooleanField(default=False)),
                ('business_egreso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='purchases', to='ingresos.BusinessLine')),
                ('compra_egreso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='purchases', to='egresos.Compras')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchases', to='ingresos.Company')),
                ('provider_egreso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchases', to='egresos.Provider')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('weigth', models.DecimalField(decimal_places=2, max_digits=10)),
                ('animal_ref', models.CharField(max_length=100)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='egresos.Purchase')),
            ],
        ),
        migrations.AddField(
            model_name='compras',
            name='proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='compras', to='egresos.Provider'),
        ),
    ]
