from django.db import models

# Create your models here.
class Tipos(models.Model):
    tipo = models.CharField(max_length=40)
    renta = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.tipo}"
    
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = ['tipo']

class Instrumentos(models.Model):
    ticker = models.CharField(max_length=6)
    tipo =  models.CharField(max_length=6)
    descripcion = models.CharField(max_length=50, db_index=True)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.descripcion}"
    
    class Meta:
        verbose_name= "Instrumento"
        verbose_name_plural = "Instrumentos"
        ordering = ['tipo','descripcion']

class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.email}, {self.apellido}, {self.nombre} "
    
    class Meta:
        verbose_name= "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['apellido']


class Operaciones(models.Model):
    tipo = models.CharField(max_length=15)
    email = models.EmailField()
    nominales = models.IntegerField()
    ticker = models.CharField(max_length=6)
    fecha = models.DateField() 

    def __str__(self):
        return f"{self.fecha}, {self.ticker}, {self.email} "  	
    
    class Meta:
        verbose_name= "Operación"
        verbose_name_plural = "Operaciones"
        ordering = ['fecha']