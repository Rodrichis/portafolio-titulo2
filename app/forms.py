from django import forms
from .models import Departamento, Persona
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class FormRegistro(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = ['nombre', 'constrasenia',]


class FormRegistroPersona(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ['rut','nombre','apellido','email','constrasenia','telefono',]

class FormRegistroDepartamento(forms.ModelForm):
    class Meta:

        model=Departamento
        fields = '__all__'

    