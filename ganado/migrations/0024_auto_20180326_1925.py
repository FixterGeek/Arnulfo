# Generated by Django 2.0.1 on 2018-03-26 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganado', '0023_auto_20180323_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='arete_rancho',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]