from django.db import models
from django.contrib.auth.models import User


# MATERIAS
class Materia(models.Model):

    nombre = models.CharField(max_length=100)

    semestre = models.IntegerField()

    creditos = models.IntegerField()

    def __str__(self):

        return self.nombre


# INGLES
class Ingles(models.Model):

    nivel = models.CharField(max_length=50)

    descripcion = models.TextField()

    def __str__(self):

        return self.nivel


# HORARIOS
class Horario(models.Model):

    materia = models.CharField(max_length=100)

    profesor = models.CharField(max_length=100)

    salon = models.CharField(max_length=50)

    hora = models.CharField(max_length=50)

    def __str__(self):

        return self.materia


# PERFIL
class Perfil(models.Model):

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    foto = models.ImageField(
        upload_to='perfiles/',
        blank=True,
        null=True
    )

    nombre_completo = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):

        return self.usuario.username