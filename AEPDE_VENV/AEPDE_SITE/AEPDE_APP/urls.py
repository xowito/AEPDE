from django.urls import path
from .views import * 

urlpatterns = [
    path('', home, name="home"),
    path('agregar_productos',agregar_productos, name="agregar_productos")
]