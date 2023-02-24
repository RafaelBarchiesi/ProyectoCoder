from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Curso(models.Model):

    def __str__(self):

        return f"Nombre: {self.nombre} ------- Camada:{self.camada} "

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    comision = models.IntegerField(default=23)
    

class Estudiante(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()

class Profesor(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField(max_length=45)
    profesion = models.CharField(max_length=60)
    edad = models.IntegerField(default=21)

class Entregables(models.Model):

    nombre = models.CharField(max_length=60)
    fechaEntrega = models.DateField()
    entregado = models.CharField(max_length=50, default="SI")

class Avatar(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avateres", null=True, blank=True)


                                
