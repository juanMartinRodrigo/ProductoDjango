from django.contrib import admin
from proyecto.models import *

class ProductoInline(admin.TabularInline):
    model = Producto

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', ]

    search_fields = ['nombre', 'telefono',]

class ProductoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Drescripcion',{
            'fields': ('nombre',)
        }),
        ('Variables',{
            'fields': ('stock', 'precio',)
        }),
        ('Detalles',{
            'fields': ('categoria', 'proveedor', )
        }),
    )

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'web', 'direccion']

    search_fields = ['nombre', 'telefono',]

    inlines = [ProductoInline,]
class VentaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'producto', 'cantidad', 'monto_final', 'fecha','des', ]

    #exclude = ['montoFinal']

# Register your models here.
admin.site.register(Venta, VentaAdmin,)
admin.site.register(Cliente, ClienteAdmin,)
admin.site.register(Proveedor, ProveedorAdmin,)
admin.site.register(Producto, ProductoAdmin,)
admin.site.register(Categoria,)
admin.site.register(Direccion,)