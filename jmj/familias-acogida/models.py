# Aqui se definen el modelo y las relaciones de los datos
#  Modelos son la estructura de la db + logica de negocio

#MVC

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)