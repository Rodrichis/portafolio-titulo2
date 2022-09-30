from django.urls import path
from .views import home, registro, ingresar, arrendar, reserva,departamentos,eliminar_departamento,Cdepartamentos

urlpatterns = [
    path('',home , name="home"), 
    path('registro/',registro , name="registro"),
    path('ingresar/',ingresar , name="ingresar"),
    path('arrendar/',arrendar , name="arrendar"),
    path('reserva/',reserva , name="reserva"),
    path('departamentos/',departamentos , name="departamentos"),
    path('Cdepartamentos/',Cdepartamentos , name="Cdepartamentos"),
    path('eliminar_departamento/<id_departamento>/', eliminar_departamento , name ="eliminar_departamento"),
   
]