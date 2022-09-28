# Generated by Django 4.1 on 2022-09-25 21:43

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
            name='Empresa',
            fields=[
                ('emp_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('nit', models.CharField(max_length=150, unique=True)),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
                ('fecha_creacion_emp', models.DateField(auto_now=True)),
                ('nom_emp', models.CharField(max_length=25, verbose_name='Nombre Empresa')),
                ('sec_prod', models.CharField(max_length=25, verbose_name='Senctor Productivo')),
                ('ciudad', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('telefono', models.CharField(max_length=100, verbose_name='Telefono')),
                ('usu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
