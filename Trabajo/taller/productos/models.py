from django.db import models

# Create your models here.


class Contacto(models.Model):
    nombre=models.CharField(max_length=30)
    apellidoP=models.CharField(max_length=30)
    apellidoM=models.CharField(max_length=30)
    rut=models.CharField(max_length=10)
    direccion=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    phone=models.IntegerField(max_length=11)
    mensaje=models.CharField(max_length=300)