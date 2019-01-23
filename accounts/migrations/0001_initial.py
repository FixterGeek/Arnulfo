

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.BooleanField(default=False, help_text='Selecciona si este usuario usará la sección administrativa')),
                ('ganado', models.BooleanField(default=False, help_text='Selecciona si este usuario usará la sección del Ganado')),
                ('vacunas', models.BooleanField(default=False, help_text='Selecciona si este usuario usará la sección de vacunas')),
                ('alimentos', models.BooleanField(default=False, help_text='Selecciona si este usuario usará la sección del alimentos')),
                ('cerdos', models.BooleanField(default=False, help_text='Selecciona si este usuario usará la sección del cerdos')),
                ('aves', models.BooleanField(default=False, help_text='Selecciona si este usuario usará la sección del aves')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
