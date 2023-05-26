from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Persona,Ciudad,TipoDocumento
from .forms import PersonaForm

# Create your views here.
def index(request):
    ciudades = Ciudad.objects.all()
    personas = Persona.objects.all()
    tipos_documento = TipoDocumento.objects.all()
    template=loader.get_template('persona/index.html')
    context={
        'ciudades':ciudades,
        'personas':personas,
        'tipos_documento':tipos_documento,
    }
    return HttpResponse(template.render(context,request))

def new_persona(request):
    if request.method=='POST':
        form=PersonaForm(request.POST)
        if form.is_valid():
            nombres=form.cleaned_data['nombres']
            apellidos=form.cleaned_data['apellidos']
            documento=form.cleaned_data['documento']
            fecha_nac=form.cleaned_data['fecha_nac']
            email=form.cleaned_data['email']
            telefono=form.cleaned_data['telefono']
            usuario=form.cleaned_data['usuario']
            contrasena=form.cleaned_data['contrasena']
            tipodoc=form.cleaned_data['id_tipo_documento']
            residencia=form.cleaned_data['lugar_residencia']
            persona=Persona(nombres=nombres,apellidos=apellidos,documento=documento,fecha_nac=fecha_nac,email=email
                            ,telefono=telefono,usuario=usuario,contrasena=contrasena,id_tipo_documento=tipodoc,lugar_residencia=residencia)
            persona.save()
            return HttpResponseRedirect(reverse('persona'))
    else:
        form = PersonaForm()
    return render(request,'persona/create_persona.html',{'form':form})