from django.contrib import admin
from .models import Contacto

# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display="nombre","apellidoP","apellidoM","rut","direccion","email","phone","mensaje"

admin.site.register(Contacto,ContactoAdmin)