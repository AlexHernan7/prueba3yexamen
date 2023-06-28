from django.contrib import admin

# Register your models here.

from .models import ContactoAdmin,Producto

admin.site.register(ContactoAdmin)

class ContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellidoP", "apellidoM", "rut", "select", "direccion", "email", "phone", "mensaje")


admin.site.register(Producto)
