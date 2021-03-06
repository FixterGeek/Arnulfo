

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine', models.CharField(max_length=100)),
                ('typeofv', models.CharField(max_length=100)),
                ('dose', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('unity', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('concentration', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
