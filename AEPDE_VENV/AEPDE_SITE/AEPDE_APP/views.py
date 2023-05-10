from django.shortcuts import render,  redirect, get_object_or_404
from .forms import formulario_agregar_producto
from .models import Producto
from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout 
from django.contrib.auth.forms import AuthenticationForm
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
