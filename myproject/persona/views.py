from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.urls import reverse
from .models import Persona,Ciudad,TipoDocumento
from .forms import PersonaForm, CiudadForm, TipoDocForm

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
            residencia=form.cleaned_data.get('ciudad')
            persona=Persona(nombres=nombres,apellidos=apellidos,documento=documento,fecha_nac=fecha_nac,email=email
                            ,telefono=telefono,usuario=usuario,contrasena=contrasena,id_tipo_documento=tipodoc,ciudad=residencia)
            persona.save()
            next = request.POST.get('next','/persona')
            return HttpResponseRedirect(next)
    else:
        form = PersonaForm()
        return render(request,'persona/create_persona.html',{'form':form})

def delete_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    context = {'persona': persona}    

    if request.method=='GET':
        persona.delete()
        messages.success(request,  'Se ha eliminado a la persona exitosamente')
        next = request.POST.get('next','/persona')
        return HttpResponseRedirect(next)

    
def update_persona(request, id):
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
            Persona.objects.filter(pk=id).update(nombres=nombres,apellidos=apellidos,documento=documento,fecha_nac=fecha_nac,email=email
                            ,telefono=telefono,usuario=usuario,contrasena=contrasena,id_tipo_documento=tipodoc,lugar_residencia=residencia)
            next = request.POST.get('next','/persona')
            return HttpResponseRedirect(next)
    else:
        form = PersonaForm()
        return render(request,'persona/update_persona.html',{'form':form})
    
def new_ciudad(request):
    if request.method=='POST':
        form=CiudadForm(request.POST)
        if form.is_valid():
            nombre=form.cleaned_data['nombre']
            descripcion=form.cleaned_data['descripcion']
            ciudad=Ciudad(nombre=nombre,descripcion=descripcion)
            ciudad.save()
            next = request.POST.get('next','/persona')
            return HttpResponseRedirect(next)
    else:
        form = CiudadForm()
        return render(request,'persona/create_ciudad.html',{'form':form})

def delete_ciudad(request, id):
    ciudad = get_object_or_404(Ciudad, pk=id)
    context = {'ciudad': ciudad}    

    if request.method=='GET':
        ciudad.delete()
        messages.success(request,  'Se ha eliminado a la ciudad exitosamente')
        next = request.POST.get('next','/persona')
        return HttpResponseRedirect(next)

    
def update_ciudad(request, id):
    if request.method=='POST':
        form=CiudadForm(request.POST)
        if form.is_valid():
           nombre=form.cleaned_data['nombre']
           descripcion=form.cleaned_data['descripcion']
           Ciudad.objects.filter(pk=id).update(nombre=nombre,descripcion=descripcion)
           next = request.POST.get('next','/persona')
           return HttpResponseRedirect(next)
    else:
        form = CiudadForm()
        return render(request,'persona/update_ciudad.html',{'form':form})
    
def new_tipodoc(request):
    if request.method=='POST':
        form=TipoDocForm(request.POST)
        if form.is_valid():
            nombre=form.cleaned_data['nombre']
            descripcion=form.cleaned_data['descripcion']
            tipodoc=TipoDocumento(nombre=nombre,descripcion=descripcion)
            tipodoc.save()
            next = request.POST.get('next','/persona')
            return HttpResponseRedirect(next)
    else:
        form = TipoDocForm()
        return render(request,'persona/create_tipodoc.html',{'form':form})

def delete_tipodoc(request, id):
    tipodoc = get_object_or_404(TipoDocumento, pk=id)
    context = {'tipodoc': tipodoc}    

    if request.method=='GET':
        tipodoc.delete()
        messages.success(request,  'Se ha eliminado a el tipo de documento exitosamente')
        next = request.POST.get('next','/persona')
        return HttpResponseRedirect(next)

    
def update_tipodoc(request, id):
    if request.method=='POST':
        form=TipoDocForm(request.POST)
        if form.is_valid():
           nombre=form.cleaned_data['nombre']
           descripcion=form.cleaned_data['descripcion']
           TipoDocumento.objects.filter(pk=id).update(nombre=nombre,descripcion=descripcion)
           next = request.POST.get('next','/persona')
           return HttpResponseRedirect(next)
    else:
        form = TipoDocForm()
        return render(request,'persona/update_tipodoc.html',{'form':form})