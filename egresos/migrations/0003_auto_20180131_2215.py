# Generated by Django 2.0.1 on 2018-01-31 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egresos', '0002_auto_20180130_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='kg_total',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='total',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='units',
        ),
        migrations.AddField(
            model_name='purchase',
            name='business_line',
            field=models.CharField(blank=True, choices=[('Cerdos', 'Cerdos'), ('Ganado', 'Ganado'), ('Granos', 'Granos'), ('Planta de alimentos', 'Planta de alimentos'), ('Campo', 'Campo')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='no_check',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchase_check',
            field=models.BooleanField(default=False),
        ),
    ]
