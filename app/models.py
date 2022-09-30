# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acompaniante(models.Model):
    id_acompaniante = models.FloatField(primary_key=True)
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    telefono = models.FloatField(blank=True, null=True)
    persona_rut = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')

    class Meta:
        managed = False
        db_table = 'acompaniante'



class Comuna(models.Model):
    id_comuna = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region')

    class Meta:
        managed = False
        db_table = 'comuna'


class Departamento(models.Model):
    id_departamento = models.FloatField(primary_key=True)
    numero_depto = models.FloatField()
    acondicionado = models.CharField(max_length=1)
    direccion = models.CharField(max_length=200)
    habitaciones = models.FloatField()
    banios = models.FloatField()
    superficie_total = models.FloatField()
    valor = models.FloatField()
    descripcion = models.CharField(max_length=200)
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region')
    
    class Meta:
        managed = False
        db_table = 'departamento'

    def __str__(self):
        return self.descripcion
    

class DetalleInv(models.Model):
    id_detalle_inv = models.FloatField(primary_key=True)
    departamento_id_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_id_departamento')
    inventario = models.ForeignKey('Inventario', models.DO_NOTHING)
    

    class Meta:
        managed = False
        db_table = 'detalle_inv'




class Fotos(models.Model):
    id_fotografia = models.FloatField(primary_key=True)
    departamento_id_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_id_departamento')
    foto = models.ImageField(upload_to="Fotos", null=True)

    class Meta:
        managed = False
        db_table = 'fotos'


class Inventario(models.Model):
    id_inventario = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=100)
    valor = models.FloatField()
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'inventario'


class Persona(models.Model):
    id_persona = models.FloatField(primary_key=True)
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    constrasenia = models.CharField(max_length=100)
    telefono = models.FloatField()
    tipo_usuario = models.FloatField()

    class Meta:
        managed = False
        db_table = 'persona'

    def __str__(self):
        return self.nombre

class Region(models.Model):
    id_region = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'region'

    def __str__(self):
        return self.descripcion

class Reserva(models.Model):
    id_reserva = models.FloatField(primary_key=True)
    nombre_usuario = models.CharField(max_length=100)
    cant_dias = models.FloatField()
    valor_servicios = models.FloatField()
    direccion_depto = models.CharField(max_length=100)
    numero_depto = models.FloatField()
    servicios_extra = models.CharField(max_length=100)
    persona_rut = models.ForeignKey(Persona, models.DO_NOTHING, db_column='persona_rut')
    valor_reserva = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    departamento_id_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_id_departamento')

    class Meta:
        managed = False
        db_table = 'reserva'


class Servicio(models.Model):
    id_servicio = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    reserva_id_reserva = models.ForeignKey(Reserva, models.DO_NOTHING, db_column='reserva_id_reserva')

    class Meta:
        managed = False
        db_table = 'servicio'


class TipoUsuario(models.Model):
    id_usuario = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    persona_rut = models.ForeignKey(Persona, models.DO_NOTHING, db_column='id_persona')

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Tour(models.Model):
    id_tour = models.FloatField(primary_key=True)
    nombre_encargado = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    servicio_id_servicio = models.ForeignKey(Servicio, models.DO_NOTHING, db_column='servicio_id_servicio')

    class Meta:
        managed = False
        db_table = 'tour'


class Transporte(models.Model):
    id_transporte = models.FloatField(primary_key=True)
    direccion = models.CharField(max_length=200)
    horario = models.CharField(max_length=100)
    vehiculo = models.CharField(max_length=100)
    conductor = models.CharField(max_length=100)
    servicio_id_servicio = models.ForeignKey(Servicio, models.DO_NOTHING, db_column='servicio_id_servicio')

    class Meta:
        managed = False
        db_table = 'transporte'
