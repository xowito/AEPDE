from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class formulario_agregar_producto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class formulario_agregar_tarifa(forms.ModelForm):
    class Meta:
        model = Tarifa
        fields = '__all__'
        
class formulario_crear_oferta(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = '__all__'
        
class formulario_reclamo(forms.ModelForm):
    class Meta:
        model = Reclamo
        fields = '__all__'