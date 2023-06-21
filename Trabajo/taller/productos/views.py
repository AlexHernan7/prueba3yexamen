from django.shortcuts import render

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