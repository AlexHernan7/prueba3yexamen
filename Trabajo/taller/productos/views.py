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


def enviarMSJ(request):
    a = request.POST['nombre']
    b = request.POST['apellidoP']
    c = request.POST['apellidoM']
    d = request.POST['rut']
    e = request.POST['select']
    f = request.POST['direccion']
    g = request.POST['email']
    h = request.POST['phone']
    i = request.POST['mensaje']
    
    datos = ContactoAdmin(nombre=a, apellidoP=b, apellidoM=c, rut=d, select=e, direccion=f, email=g, phone=h, mensaje=i)
    datos.save()
    
    return redirect("/")