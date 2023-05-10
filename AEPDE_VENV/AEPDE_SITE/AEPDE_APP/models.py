from django.db import models

# Create your models here.
class Sucursal(models.Model):
    cod_sucursal = models.CharField(primary_key=True,max_length=25)
    direccion = models.CharField(max_length=500)
    nombre = models.CharField(max_length=500)
    def __str__(self):
	    return self.nombre + '-'+ self.direccion
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
    def __str__(self):
	    return self.codigo
class Meta:
    ordering = ["precio"]
    
class Productor(models.Model):
    cod_productor = models.CharField(primary_key=True,max_length=9)
    nombre_empresa = models.CharField(max_length=500)
    