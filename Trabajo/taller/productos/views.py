from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'productos/Index.html')

def nosotros(request):
    return render(request, 'productos/nosotros.html')

def contacto(request):
    return render(request, 'productos/contacto.html')

def galeria(request):
    return render(request, 'productos/galeria.html')

def vehiculos(request):
    return render(request, 'productos/vehiculos.html')


def enviarMSJ(request):
    a=request.POST['nombre']
    b=request.POST['apellidoP']
    c=request.POST['apellidoM']
    d=request.POST['rut']
    e=request.POST['direccion']
    f=request.POST['email']
    g=request.POST['phone']
    h=request.POST['mensaje']
    datos=enviarMSJ(nombre=a,apellidoP=b,apellidoM=c,rut=d,direccion=e,email=f,phone=g,mensaje=h)
    datos.save()
    return redirect("/")