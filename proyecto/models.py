from django.db import models

# Create your models here.
class Direccion(models.Model):
    calle = models.CharField(max_length=50, default="")
    comuna = models.CharField(max_length=50, default="")
    ciudad = models.CharField(max_length=50, default="")
    numero = models.IntegerField()
    def __str__(self):
        return str(self.ciudad)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, default="")
    descripcion = models.CharField(max_length=50, default="")
    def __str__(self):
        return str(self.nombre + " " + self.descripcion)

class Producto(models.Model):
    nombre = models.CharField(max_length=50, default="")
    precio =  models.FloatField()
    stock =  models.IntegerField()
    categoria = models.ForeignKey('Categoria', default = None, on_delete=models.CASCADE)
    proveedor = models.ForeignKey('Proveedor', default = None, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nombre)

class Proveedor(models.Model):
    telefono = models.IntegerField()
    nombre = models.CharField(max_length=50, default="")
    web = models.CharField(max_length=50, default="")
    rut = models.IntegerField()
     direccion = models.ForeignKey('Direccion', default = None, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nombre)

class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    descuento = models.BooleanField()
    cantidad = models.IntegerField()
    cliente = models.ForeignKey('Cliente', default = None, on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', default = None, on_delete=models.CASCADE)
    def monto_final():
        self.monto = self.producto.precio * self.cantidad
        return self.monto

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, default="")
    direccion = models.ManyToManyField('Direccion')
    telefono = models.IntegerField()
    rut = models.IntegerField()
    def __str__(self):
        return str(self.nombre + " " + self.direccion)
