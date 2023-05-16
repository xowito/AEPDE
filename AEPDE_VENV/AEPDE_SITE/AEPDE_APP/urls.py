from django.urls import path
from .views import * 

urlpatterns = [
    path('', home, name="home"),
    path('agregar_productos',agregar_productos, name="agregar_productos"),
    path('register',register_request, name="register"),
    path('login',login_request, name="login"),
    path('logout',logout_request,name="logout"),
    path('catalogo_productor',catalogo_productor,name="catalogo_productor"),
    path('detalle_producto/<id>',detalle_producto,name="detalle_producto"),
    path('agregar_favorito/<int:id>/', agregar_favorito, name='agregar_favorito'),
    path('agregar_al_carrito/', agregar_al_carrito, name='agregar_al_carrito'),
]