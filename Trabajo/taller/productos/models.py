from django.db import models

# Create your models here.

opciones_genero = [
    (0,'helicoptero apache'),
    (1,'Femenino'),
    (2,'Masculino')
]

class ContactoAdmin(models.Model):
    nombre=models.CharField(max_length=30)
    apellidoP=models.CharField(max_length=30)
    apellidoM=models.CharField(max_length=30)
    rut=models.CharField(max_length=11)
    genero=models.IntegerField(null=False, blank=False,choices=opciones_genero
                               ,default=1)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(max_length=60)
    phone=models.CharField(max_length=11)
    mensaje=models.CharField(max_length=300)

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellidoP) 
    

# clase productos
class Producto(models.Model):
    nombreP=models.CharField(max_length=30)
    categoriaP=models.CharField(max_length=30)
    modelovehiculoP=models.CharField(max_length=30)
    precioP=models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return str(self.nombreP)+" "+str(self.precioP) 

