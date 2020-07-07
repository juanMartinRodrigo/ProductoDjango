from django.db import models

# Create your models here.
class Direccion(models.Model):
    calle = models.CharField(max_length=50, default="")
    comuna = models.CharField(max_length=50, default="")
    ciudad = models.CharField(max_length=50, default="")
    numero = models.IntegerField(null = True)
    
    def __str__(self):
        return str(self.ciudad)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, default="")
    descripcion = models.CharField(max_length=50, default="")

    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    nombre = models.CharField(max_length=50, default="")
    precio =  models.FloatField(null = True)
    stock =  models.IntegerField(null = True)
    categoria = models.ForeignKey('Categoria', default = None, on_delete=models.CASCADE)
    proveedor = models.ForeignKey('Proveedor', default = None, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.nombre)

class Proveedor(models.Model):
    telefono = models.IntegerField(null = True)
    nombre = models.CharField(max_length=50, default="")
    web = models.CharField(max_length=50, default="")
    rut = models.IntegerField(null = False, unique = True)
    direccion = models.ForeignKey('Direccion', default = None, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.nombre)

class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    descuento = models.BooleanField(null = True)
    cantidad = models.IntegerField(null = True)
    cliente = models.ForeignKey('Cliente', default = None, on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', default = None, on_delete=models.CASCADE)
    montoFinal = models.FloatField()
    
    def des(self):
        if self.descuento == True:
            return True
        else:
            return False
    
    des.boolean = True
    des.short_description = "Tiene descuento"

    def monto_final(self):
        self.montoFinal = self.producto.precio * self.cantidad
        return self.montoFinal

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, default="")
    direccion = models.ManyToManyField('Direccion')
    telefono = models.IntegerField(null = True)
    rut = models.IntegerField(null = False, unique = True)
    
    def __str__(self):
        return str(self.nombre)