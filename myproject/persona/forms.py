from django import forms 
from .models import Persona,Ciudad,TipoDocumento

class PersonaForm(forms.ModelForm):
    class Meta:
        model =  Persona

        fields=[
            'nombres',
            'apellidos',
            'documento',
            'fecha_nac',
            'email',
            'telefono',
            'usuario',
            'contrasena',
            'id_tipo_documento',
            'ciudad',
        ]

        labels={
            'nombres':'Nombres',
            'apellidos':'Apellidos',
            'documento':'Documento',
            'fecha_nac':'Fecha_Nacimiento',
            'email':'Email',
            'telefono':'Telefono',
            'usuario':'Usuario',
            'contrasena':'Contrasena',
            'id_tipo_documento':'Tipodoc',
            'ciudad':'Residencia',
        }

        widgets = {
            'nombres': forms.TextInput(attrs={'class':'form-control','required':''}),
            'apellidos':forms.TextInput(attrs={'class':'form-control','required':''}),
            'documento':forms.TextInput(attrs={'class':'form-control','required':''}),
            'fecha_nac':forms.TextInput(attrs={'class':'form-control','required':''}),
            'email':forms.TextInput(attrs={'class':'form-control','required':''}),
            'telefono':forms.TextInput(attrs={'class':'form-control','required':''}),
            'usuario':forms.TextInput(attrs={'class':'form-control','required':''}),
            'contrasena':forms.TextInput(attrs={'class':'form-control','required':''}),
            'id_tipo_documento':forms.TextInput(attrs={'class':'form-control','required':''}),
            'ciudad':forms.TextInput(attrs={'class':'form-control','required':''}),
        }

class CiudadForm(forms.ModelForm):
    class Meta:
        model =  Ciudad

        fields=[
            'nombre',
            'descripcion',
        ]

        labels={
            'nombres':'Nombre',
            'descripcion':'Descripcion'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','required':''}),
            'descripcion':forms.TextInput(attrs={'class':'form-control','required':''}),
        }

class TipoDocForm(forms.ModelForm):
    class Meta:
        model =  Ciudad

        fields=[
            'nombre',
            'descripcion',
        ]

        labels={
            'nombres':'Nombre',
            'descripcion':'Descripcion'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','required':''}),
            'descripcion':forms.TextInput(attrs={'class':'form-control','required':''}),
        }