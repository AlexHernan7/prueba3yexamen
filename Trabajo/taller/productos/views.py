from django.shortcuts import render, redirect
from .models import ContactoAdmin

# Create your views here.
def index(request):
    return render(request, 'productos/Index.html')

def nosotros(request):
    return render(request, 'productos/nosotros.html')

def contacto(request):
    productos= ContactoAdmin.objects.raw('SELECT * from productos_contactoadmin')
    print(productos)
    context={'productos':productos}
    return render(request, 'productos/contacto.html',context)

def galeria(request):
    return render(request, 'productos/galeria.html')

def vehiculos(request):
    return render(request, 'productos/vehiculos.html')


def registrarComentario(request):
    nombre=request.POST['nombre']
    apellidoP=request.POST['apellidoP']
    apellidoM=request.POST['apellidoM']
    rut=request.POST['rut']
    genero=request.POST['genero']
    direccion=request.POST['direccion']
    email=request.POST['email']
    phone=request.POST['phone']
    mensaje=request.POST['mensaje']

    comentario=ContactoAdmin.objects.create(nombre=nombre,apellidoP=apellidoP,
                                            apellidoM=apellidoM,rut=rut,genero=genero,direccion=direccion,
                                            email=email,phone=phone,mensaje=mensaje)

    return redirect("/mycontacto")