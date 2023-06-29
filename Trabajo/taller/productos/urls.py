from django.urls import path
from . import views

from productos.views import agregar_producto, eliminar_producto, restar_producto, limpiar_carrito


urlpatterns = [
    path('', views.index, name='index'),
    path('mynosotros', views.nosotros, name='nosotros'),
    path('mycontacto', views.contacto, name='contacto'),
    path('mygaleria', views.galeria, name="galeria"),
    path('myvehiculo', views.vehiculos, name="vehiculos"),
    path('registrarComentario/',views.registrarComentario, name='registrarComentario'),
    path('register/',views.register, name='register'),
    path('agregar-crud/', views.agregarCrud, name='agregar_crud'),
    path('listar-crud/', views.listarCrud, name='listar_crud'),
    path('modificar-crud/<id>/', views.modificarCrud, name='modificar_crud'),
    path('eliminar-crud/<id>/', views.eliminar_crud, name='eliminar_crud'),

    
    path('mytienda/', views.tienda, name='tienda'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]

