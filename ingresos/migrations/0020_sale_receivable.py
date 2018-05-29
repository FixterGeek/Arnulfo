# Generated by Django 2.0.1 on 2018-05-21 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingresos', '0019_auto_20180518_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='receivable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sales', to='ingresos.CuentaBanco'),
        ),
    ]
