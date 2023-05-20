from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Sucursal(models.Model):
    cod_sucursal = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=500)
    nombre = models.CharField(max_length=500)
    def __str__(self):
	    return self.nombre + '-'+ self.direccion
 
class Productor(models.Model):
    cod_productor = models.IntegerField(primary_key=True)
    nombre_empresa = models.CharField(max_length=500)
    telefono_contacto = models.IntegerField()
    correo_contacto = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_empresa


contacto_productor = [
    ('1',Productor.correo_contacto)
    ]
print (contacto_productor)
class Producto(models.Model):
    
    tipo_producto = [
        ('1','Frutas'),
        ('2','Verduras'),
        ('3','Cereales')
    ]
    codigo = models.IntegerField(primary_key=True)
    imagen = models.ImageField(upload_to='images')
    descripcion = models.CharField(max_length=50)
    tipo = models.CharField(default=1, max_length=1, choices=tipo_producto)
    precio = models.IntegerField()
    stock = models.IntegerField()
    fecha_produccion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento_prod = models.DateTimeField(auto_now=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    cod_productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    def __str__(self):
	    return self.codigo
class Meta:
    ordering = ["precio"]


class Favorito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} favorited {self.producto.descripcion}'

    def get_absolute_url(self):
        return reverse('detalle_producto', args=[str(self.producto.codigo)])
    
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Carrito del usuario {self.usuario.username}"

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.descripcion} en el carrito de {self.carrito.usuario.username}"
    
class Transportista(models.Model):
    codigo_transportista = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.codigo_transportista} - {self.nombre}"
    
     
class Tarifa(models.Model):
    categoria = models.CharField(max_length=50)
    monto = models.IntegerField(default=1)
    codigo_transportista = models.ForeignKey(Transportista, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.categoria} - {self.monto}"
    class Meta:
        permissions = [
            ("puede_acceder_url","Puede acceder a la URL")
        ]
    
    
          

    

     