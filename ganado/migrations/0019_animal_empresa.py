# Generated by Django 2.0.1 on 2018-02-28 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingresos', '0009_auto_20180226_1927'),
        ('ganado', '0018_auto_20180227_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animals', to='ingresos.Company'),
        ),
    ]