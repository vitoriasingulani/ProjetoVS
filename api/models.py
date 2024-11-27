from django.db import models

class Usuarios(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    idade = models.IntegerField()