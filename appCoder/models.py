from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()

    def __str__(self) -> str:
        return f' Nombre: {self.nombre} - Camada: {self.camada} '

class Estudiante(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()

    def __str__(self) -> str:
        return f' Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} '

class Profesor(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    profesion=models.CharField(max_length=40)

    def __str__(self) -> str:
        return f' Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profecion: {self.profesion}'


class Entregable(models.Model):

    nombre=models.CharField(max_length=40)
    fechaDentrega=models.DateField()
    entregado=models.BooleanField()

