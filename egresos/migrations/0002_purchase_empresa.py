# Generated by Django 2.0.1 on 2018-07-07 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingresos', '0002_auto_20180707_1957'),
        ('egresos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchases', to='ingresos.Company'),
        ),
    ]
