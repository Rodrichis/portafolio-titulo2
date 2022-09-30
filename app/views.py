from django.shortcuts import render, redirect
from .models import Departamento, Region 
from .forms import FormRegistroPersona,FormRegistroDepartamento
from django.contrib.auth import authenticate
# Create your views here.

def home(request):
    departamento = Departamento.objects.all()
    region = Region.objects.all()
    data = {

        'departamento': departamento,
        

    }
    return render(request, 'app/home.html', data)

def registro(request):
    data = {
        'form1' : FormRegistroPersona()
    }

    if request.method == 'POST':
        formulario = FormRegistroPersona(data=request.POST)
        if formulario.is_valid():
            
            formulario.save()
            data ["mensaje"] = "Usuario Registrado"
        else:
            data["form1"] = formulario


    return render(request, 'app/registro.html',data)

def ingresar(request):
    return render(request, 'app/ingresar.html')

def arrendar(request):
    return render(request, 'app/arrendar.html')

def reserva(request):
    return render(request, 'app/reserva.html')

def departamentos(request):
    departamento = Departamento.objects.all()
    
    data = {

        'departamento': departamento,
        

    }
    return render(request, 'app/departamento.html',data)

def Cdepartamentos(request):
    departamento = Departamento.objects.all()
    
    data = {
        'form1' : FormRegistroDepartamento()
    }

    if request.method == 'POST':
        formulario = FormRegistroDepartamento(data=request.POST)
        if formulario.is_valid():
            
            formulario.save()
            data ["mensaje"] = "Departamento Registrado"
        else:
            data["form2"] = formulario
    return render(request, 'app/Cdepartamento.html',data)

def eliminar_departamento(request,id_departamento):
    departamento=Departamento.objects.get(id_departamento=id_departamento)
    departamento.delete()

    return redirect(to="departamentos")

