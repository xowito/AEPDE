from django import forms
from django.contrib.admin import widgets

from .models import *

class formulario_agregar_producto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'