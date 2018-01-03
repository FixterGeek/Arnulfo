# Generated by Django 2.0 on 2018-01-03 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egresos', '0002_remove_purchaseitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseitem',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
