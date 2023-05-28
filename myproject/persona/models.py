from django.db import models

# Create your models here.

class TipoDocumento(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=30)
    def str(self):
        return self.nombre

class Ciudad(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50) 
    def str(self):
        return self.nombre

class Persona(models.Model):
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    documento=models.CharField(max_length=20)
    fecha_nac=models.DateField()
    email=models.CharField(max_length=30)
    telefono=models.CharField(max_length=20)
    usuario=models.CharField(max_length=50)
    contrasena=models.CharField(max_length=50)
    id_tipo_documento=models.ForeignKey(TipoDocumento, on_delete=models.CASCADE) 
    lugar_residencia=models.ForeignKey(Ciudad, on_delete=models.CASCADE)