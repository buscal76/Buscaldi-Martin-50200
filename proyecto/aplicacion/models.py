from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#__________________________________________________________________________Tipos
class Tipos(models.Model):
    tipo = models.CharField(max_length=40)
    renta = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.tipo}, {self.renta}"
    
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = ['tipo']

#__________________________________________________________________________Instrumentos
class Instrumentos(models.Model):
    ticker = models.CharField(max_length=6)
    tipo =  models.CharField(max_length=40)
    descripcion = models.CharField(max_length=50, db_index=True)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.ticker},{self.tipo},{self.descripcion}"
    
    class Meta:
        verbose_name= "Instrumento"
        verbose_name_plural = "Instrumentos"
        ordering = ['tipo','descripcion']

#__________________________________________________________________________Cuentas
class Cuentas(models.Model):
    cuenta_comitente = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    apertura = models.DateField() 
    email = models.EmailField()
        
    def __str__(self):
        return f"{self.cuenta_comitente}, {self.apellido}, {self.nombre},"
    
    class Meta:
        verbose_name= "Cuenta"
        verbose_name_plural = "Cuentas"
        ordering = ['cuenta_comitente']

#__________________________________________________________________________Operaciones
class Operaciones(models.Model):
    tipo = models.CharField(max_length=15)
    cuenta = models.IntegerField()
    nominales = models.IntegerField()
    ticker = models.CharField(max_length=6)
    fecha = models.DateField() 

    def __str__(self):
        return f"{self.fecha}, {self.ticker}, {self.cuenta} "  	
    
    class Meta:
        verbose_name= "Operación"
        verbose_name_plural = "Operaciones"
        ordering = ['fecha']

#__________________________________________________________________________Usuarios
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

#__________________________________________________________________________Avatar
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"   
