from productos.Carrito import Carrito
from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactoAdmin, Producto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import ProductoForm


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
            messages.success(request,"Te has registrado correctamente")
            return redirect('index')
    return render(request, 'registration/register.html',data)


#  Carrito

@login_required
def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'productos/tienda.html', {'productos': productos})


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("/mytienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("/mytienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("/mytienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("/mytienda")

def agregarCrud(request):
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'productos/agregarCrud.html', data)

def listarCrud(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }
    return render(request, 'productos/listarCrud.html', data)

def modificarCrud(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect("listar_crud")
        data["form"] = formulario
    return render(request, 'productos/modificarCrud.html', data)


def eliminar_crud(request, id):
   producto = get_object_or_404(Producto, id=id)
   producto.delete()
   return redirect("listar_crud") 