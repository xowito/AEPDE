from django.http import HttpRequest ,HttpResponseRedirect, JsonResponse
from django.shortcuts import render,  redirect, get_object_or_404
from .forms import formulario_agregar_producto,formulario_agregar_tarifa, formulario_crear_oferta
from .models import Producto, Productor, Favorito, Carrito ,ItemCarrito, Oferta
from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout, get_user
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import  redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from datetime import datetime
from django.db.models import Prefetch
#Vista home

def home(request):
    productos_con_oferta = Producto.objects.prefetch_related(Prefetch('oferta_set', queryset=Oferta.objects.order_by('-fecha_inicio')))
    pr = Productor.objects.all()
    p = Producto.objects.all()
    a = request.user.id
    data = {
        "producto": productos_con_oferta,
        "productor":pr,
        "as":a 
    }
    

    return render(request,"AEPDE_APP/home.html",data)

def detalle_producto(request,id):
    
    detalle = Producto.objects.get(codigo=id)
    productor = detalle.cod_productor
    sucursal = detalle.sucursal
    data = {"obj":detalle,"productor": productor,"sucursal":sucursal,}
    return render(request,'AEPDE_APP/detalle_producto.html',data)
@login_required
@permission_required('AEPDE_APP.add_producto',raise_exception=True)
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

@login_required
def agregar_favorito(request, id):
    producto = get_object_or_404(Producto, codigo=id)
    favorito, created = Favorito.objects.get_or_create(user=request.user, producto=producto)
    if created:
        messages.success(request, f"{producto.descripcion} se ha agregado a tus favoritos.")
    else:
        messages.warning(request, f"{producto.descripcion} ya está en tus favoritos.")
    return redirect('detalle_producto', id=id)


@login_required
def agregar_al_carrito(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad', 1))
        producto = get_object_or_404(Producto, codigo=producto_id)
        
        # Restar del stock del producto
        producto.stock -= cantidad
        producto.save()
        
        carrito, created = Carrito.objects.get_or_create(usuario=request.user, activo=True)
        if created:
            carrito.save()
        item, item_created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
        if not item_created:
            item.cantidad += cantidad
            item.save()
        
        messages.success(request, f"{cantidad} x {producto.descripcion} agregado al carrito.")
    return redirect('detalle_producto', id=producto_id)

@login_required
@permission_required('AEPDE_APP.add_tarifa', raise_exception=True)
def agregar_tarifa(request):
    formulario = formulario_agregar_tarifa()
    data={"form":formulario}
    if request.method == 'POST':
        formulario = formulario_agregar_tarifa(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tarifa agregada correctamente")
            return redirect(to="home")
    return render(request,"AEPDE_APP/agregar_tarifa.html",data)

@login_required
@permission_required('AEPDE_APP.add_oferta', raise_exception=True)
def crear_oferta(request, cod_producto):
    producto = Producto.objects.get(codigo=cod_producto)
    if request.method == 'POST':
        form = formulario_crear_oferta(request.POST)
        if form.is_valid():
            oferta = form.save(commit=False)
            oferta.cod_producto = producto
            oferta.save()
            # Optionally perform additional actions or redirect to a success page
            return redirect(to='home')
    else:
        form = formulario_crear_oferta()
    return render(request, 'AEPDE_APP/crear_oferta.html', {'form': form, 'producto': producto})