from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('mynosotros', views.nosotros, name='nosotros'),
    path('mycontacto', views.contacto, name='contacto'),
    path('mygaleria', views.galeria, name="galeria"),
    path('myvehiculo', views.vehiculos, name="vehiculos"),
    path('registrarComentario/',views.registrarComentario, name='registrarComentario'),
    path('register/',views.register, name='register'),
]

