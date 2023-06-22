from django.contrib import admin

# Register your models here.

from .models import ContactoAdmin
admin.site.register(ContactoAdmin)

class ContactoAdmin(admin.ModelAdmin):
    list_display="nombre","apellidoP","apellidoM","rut","direccion","email","phone","mensaje"

