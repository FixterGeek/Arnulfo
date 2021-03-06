

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('egresos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_units', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('unit_price_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('freight', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('loading_maneuver', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insumos', to='egresos.Provider')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('formula', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='planta_alimentos.Formula')),
                ('insumo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='planta_alimentos.Insumo')),
            ],
        ),
    ]
