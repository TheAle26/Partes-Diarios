from django.db import models
from django.db.models import Sum

# Create your models here.
class Lote(models.Model):
    margen = models.CharField(max_length=10,verbose_name="Margen",null=True)
    lote = models.CharField(max_length=99,verbose_name="Lote - Parcela",null=True)
    
    propietario = models.CharField(max_length=99,verbose_name="Propietario",null=True)
    volfirme =models.FloatField(default=0.0,verbose_name="Volumen Firme (m3)",null=True)
    usuario = models.CharField(max_length=99,verbose_name="Ultima modificacion",null=True)
    def __str__(self):
        return self.lote
    

class Recinto(models.Model):
    lote = models.CharField(max_length=99,verbose_name="Lote - Parcela",null=True)
    nombre = models.CharField(max_length=99,verbose_name="Nombre",null=True)
    margen = models.CharField(max_length=10,verbose_name="Margen",null=True)
    capacidad=models.FloatField(default=0.0,verbose_name="Volumen Firme (m3)",null=True)
    nombre = models.CharField(max_length=99,verbose_name="Ultima modificacion",null=True)
    usuario = models.CharField(max_length=99,verbose_name="Ultima modificacion",null=True)



    def __str__(self):
        return self.lote


class Estado_De_Aprobacion(models.Model):
    lote= models.CharField(max_length=99,verbose_name="Lote - Parcela",null=True)
    actualizacion= models.DateField(verbose_name="Fecha de Actualizacion",null=True)
    estado= models.CharField(max_length=99,verbose_name="Estado",null=True)
    denominacion= models.CharField(max_length=99,verbose_name="Denominacion",null=True)
    capacidad= models.IntegerField(verbose_name="Capacidad",null=True)
    usuario = models.CharField(max_length=99,verbose_name="Ultima modificacion",null=True)

    def __str__(self):
        return self.lote


class Maquinaria(models.Model):
    nombre = models.CharField(max_length=99,verbose_name="Nombre",null=True)
    horometro=models.FloatField(default=0.0,verbose_name="Horometro",null=True)
    def __str__(self):
        return self.nombre





    """""
    def actualizar_volumen(self):
        # Obtén el promedio de las puntuaciones de las reseñas asociadas a este restaurante
        volumen_rellenado = Viaje.objects.filter(recinto=self).aggregate(Sum('volmen'))['volumen_sum']
        
        # Si hay reseñas, actualiza la calificación del restaurante
        if volumen_rellenado is not None:
            self.volumen_restante = round(volumen_rellenado, 2)
            self.save()

esto tengo que agregar en el lugar donde se cargue le vijae
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Llama a la función para actualizar la calificación del Recinto
        self.Recinto.actualizar_volumen()


    """