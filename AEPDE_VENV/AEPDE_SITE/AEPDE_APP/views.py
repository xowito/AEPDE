from django.http import HttpRequest
from django.shortcuts import render,  redirect, get_object_or_404
from .forms import formulario_agregar_producto
from .models import Producto,Productor
from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout, get_user
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Q
#Vista home

def home(request):
    pr = Productor.objects.all()
    p = Producto.objects.all()
    a = request.user.id
    data = {
        "producto": p,
        "productor":pr,
        "as":a 
    }
    return render(request,"AEPDE_APP/home.html",data)

def detalle_producto(request,id):
    detalle = Producto.objects.get(codigo=id)
    data = {"obj":detalle}
    return render(request,'AEPDE_APP/detalle_producto.html',data)

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


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(to="home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request,"AEPDE_APP/registration/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Iniciaste sesion como {username}.")
				return redirect(to="home")
			else:
				messages.error(request,"Usuario o password incorrectos.")
		else:
			messages.error(request,"Usuario o password incorrectos.")
	form = AuthenticationForm()
	return render(request, "AEPDE_APP/registration/login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "Cerraste sesion correctamente.") 
	return redirect(to="home")


def catalogo_productor(request):
	uid = request.user.id
	p = Producto.objects.filter(Q(cod_productor=uid))
	data = {
        "producto":p 
    }	
	return render(request, "AEPDE_APP/catalogo_productor.html",data)