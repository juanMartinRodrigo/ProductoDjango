from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, default="");
    descripcion = models.CharField(max_length=50, default="");
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE);
    def __str__(self):
        return str(self.nombre + " " + self.descripcion)

class Producto(models.Model):
    nombre = models.CharField(max_length=50, default="");
    precio =  models.IntegerField();
    stock =  models.IntegerField();
    def __str__(self):
        return str(self.nombre + " " + self.precio)

class Direccion(models.Model):
    calle = models.CharField(max_length=50, default="");
    comuna = models.CharField(max_length=50, default="");
    ciudad = models.CharField(max_length=50, default="");
    numero = models.IntegerField();

class Proveedor(models.Model):
    telefono = models.IntegerField();
    nombre = models.CharField(max_length=50, default="");
    web = models.CharField(max_length=50, default="");
    direccion = models.ManyToManyField('Direccion');
    def __str__(self):
        return str(self.nombre)

class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True);
    descuento = models.IntegerField();
    cantidad = models.IntegerField();
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE);
    def __str__(self):
        return str(self.fecha + " " + self.descuento + " " + self.producto)
    def monto_final():
        monto = producto.precio * cantidad
        return monto

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, default="");
    direccion = models.ManyToManyField('Direccion');
    telefono = models.IntegerField();
    def __str__(self):
        return str(self.nombre + " " + self.direccion)
