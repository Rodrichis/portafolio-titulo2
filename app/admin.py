from django.contrib import admin
from .models import Acompaniante, Comuna, Departamento, DetalleInv, Fotos, Inventario, Persona, Region ,Reserva, Servicio, TipoUsuario, Tour, Transporte
# Register your models here.

admin.site.register(Acompaniante)
admin.site.register(Comuna)
admin.site.register(Departamento)
admin.site.register(DetalleInv)
admin.site.register(Fotos)
admin.site.register(Inventario)
admin.site.register(Persona)
admin.site.register(Region)
admin.site.register(Reserva)
admin.site.register(Servicio)
admin.site.register(TipoUsuario)
admin.site.register(Tour)
admin.site.register(Transporte)

