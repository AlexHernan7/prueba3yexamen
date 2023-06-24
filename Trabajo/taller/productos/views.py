from django.shortcuts import render, redirect
from .models import ContactoAdmin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

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

@login_required
def products(request):
    return render(request, 'core/products.html')


def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('index')
    return render(request, 'productos/registration/register.html',data)
