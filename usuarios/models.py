from django.db import models

# Create your models here.

class User(models.Model):
    """Modelo de usuario para un CRUD simple.
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    numero_celular = models.IntegerField(max_length=10, blank=False)
