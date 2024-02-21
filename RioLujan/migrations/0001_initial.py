# Generated by Django 5.0.1 on 2024-02-21 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado_De_Aprobacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote', models.CharField(max_length=99, verbose_name='Lote - Parcela')),
                ('actualizacion', models.DateField(verbose_name='Fecha de Actualizacion')),
                ('estado', models.CharField(max_length=99, verbose_name='Estado')),
                ('denominacion', models.CharField(max_length=99, verbose_name='Denominacion')),
                ('capacidad', models.IntegerField(verbose_name='Capacidad')),
                ('usuario', models.CharField(max_length=99, verbose_name='Ultima modificacion')),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('margen', models.CharField(max_length=10, verbose_name='Margen')),
                ('lote', models.CharField(max_length=99, verbose_name='Lote - Parcela')),
                ('propietario', models.CharField(max_length=99, verbose_name='Propietario')),
                ('volfirme', models.FloatField(default=0.0, verbose_name='Volumen Firme (m3)')),
                ('usuario', models.CharField(max_length=99, verbose_name='Ultima modificacion')),
            ],
        ),
        migrations.CreateModel(
            name='Maquinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=99, verbose_name='Nombre')),
                ('horometro', models.FloatField(default=0.0, verbose_name='Horometro')),
            ],
        ),
        migrations.CreateModel(
            name='Recinto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote', models.CharField(max_length=99, verbose_name='Lote - Parcela')),
                ('margen', models.CharField(max_length=10, verbose_name='Margen')),
                ('capacidad', models.FloatField(default=0.0, verbose_name='Volumen Firme (m3)')),
                ('nombre', models.CharField(max_length=99, verbose_name='Ultima modificacion')),
                ('usuario', models.CharField(max_length=99, verbose_name='Ultima modificacion')),
            ],
        ),
    ]
