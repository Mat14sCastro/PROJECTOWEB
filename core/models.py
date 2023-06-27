from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.

class TParma(models.Model):
    nombreTP = models.CharField(max_length=60)
    #ESTO ES PARA QUE SE AGREGE EL NOMBRE ARRIBA EN LA BD
    def __str__(self):
        return self.nombreTP

class Arma(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=80)
    fabricante = models.CharField(max_length=80)
    municion = models.CharField(max_length=80)
    #LO MISMO DE LA LINEA 7
    def __str__(self):
        return self.nombre


