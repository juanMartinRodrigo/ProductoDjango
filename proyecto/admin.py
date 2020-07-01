from django.contrib import admin
from proyecto.models import *

class CategoriaInline(admin.TabularInline):
    model = Categoria

class VentaInline(admin.TabularInline):
    model = Venta

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio',]
    inlines = [CategoriaInline , VentaInline, ]



# Register your models here.
admin.site.register(Producto, ProductoAdmin );
admin.site.register(Proveedor);
admin.site.register(Venta);
