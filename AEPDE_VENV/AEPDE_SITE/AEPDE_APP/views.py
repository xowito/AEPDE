from django.shortcuts import render,  redirect, get_object_or_404
from .forms import formulario_agregar_producto
from .models import Producto
from django.contrib import messages
#Vista home

def home(request):
    p = Producto.objects.all()
    data = {
        "producto": p 
    }
    return render(request,"AEPDE_APP/home.html",data)

def agregar_productos(request):
    formulario = formulario_agregar_producto()
    data={"form":formulario}
    if request.method == 'POST':
        formulario = formulario_agregar_producto(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado correctamente")
            return redirect(to="home")
    return render(request, "AEPDE_APP/agregar_productos.html",data)
