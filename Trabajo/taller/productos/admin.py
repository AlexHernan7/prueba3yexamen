from django.contrib import admin
from django.contrib.auth.models import Permission
# Register your models here.

from .models import ContactoAdmin,Producto

admin.site.register(ContactoAdmin)

class ContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellidoP", "apellidoM", "rut", "select", "direccion", "email", "phone", "mensaje")


admin.site.register(Producto)
admin.site.register(Permission)
