from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import * 
from .forms import *

# Create your views here.

def home(request):
    return render(request, "aplicacion/home.html")

def tipos(request):
    contexto = {'tipo': Tipos.objects.all()}
    return render(request, "aplicacion/tipos.html", contexto)

def instrumentos(request):
    contexto = {'instrumentos': Instrumentos.objects.all()}
    return render(request, "aplicacion/instrumentos.html", contexto)

def usuarios(request):
     contexto = {'usuario': Usuarios.objects.all()}
     return render(request, "aplicacion/usuarios.html", contexto)

def operaciones(request):
    contexto = {'operacion': Operaciones.objects.all()}
    return render(request, "aplicacion/operaciones.html", contexto)

def tiposForm(request):
    if request.method == "POST":
        miForm = TipoForm(request.POST)
        if miForm.is_valid():
            tipo_tipo = miForm.cleaned_data.get("tipo")
            tipo_renta = miForm.cleaned_data.get("renta")
            tipo = Tipos(tipo=tipo_tipo, renta=tipo_renta)
            tipo.save()
            return redirect(reverse_lazy('tipos'))
    else:
        miForm = TipoForm()
    return render(request, "aplicacion/tiposForm.html", {"form": miForm})

def operacionesForm(request):
    if request.method == "POST":
        miForm = OperacionesForm(request.POST)
        if miForm.is_valid():
            operacion_tipo = miForm.cleaned_data.get("tipo")
            operacion_email = miForm.cleaned_data.get("email")
            operacion_nominales = miForm.cleaned_data.get("nominales")
            operacion_ticker = miForm.cleaned_data.get("ticker")
            operacion_fecha = miForm.cleaned_data.get("fecha")
            operacion = Operaciones(tipo=operacion_tipo, email=operacion_email, nominales=operacion_nominales, ticker=operacion_ticker, fecha=operacion_fecha)
            operacion.save()
            return redirect(reverse_lazy('operaciones'))
    else:
        miForm = OperacionesForm()
    return render(request, "aplicacion/operacionesForm.html", {"form": miForm})

def instrumentosForm(request):
    if request.method == "POST":
        miForm = InstrumentosForm(request.POST)
        if miForm.is_valid():
            instrumento_ticker = miForm.cleaned_data.get("ticker")
            instrumento_tipo = miForm.cleaned_data.get("tipo")
            instrumento_descripcion = miForm.cleaned_data.get("descripcion")
            instrumento_precio = miForm.cleaned_data.get("precio")
            instrumento = Instrumentos(ticker=instrumento_ticker, tipo=instrumento_tipo, descripcion=instrumento_descripcion,precio=instrumento_precio)
            instrumento.save()
            return redirect(reverse_lazy('instrumentos'))
    else:
        miForm = InstrumentosForm()
    return render(request, "aplicacion/instrumentosForm.html", {"form": miForm})


def usuariosForm(request):
    if request.method == "POST":
        miForm = UsuariosForm(request.POST)
        if miForm.is_valid():
            usuario_nombre = miForm.cleaned_data.get("nombre")
            usuario_apellido = miForm.cleaned_data.get("apellido")
            usuario_email = miForm.cleaned_data.get("email")
            usuario_profesion = miForm.cleaned_data.get("profesion")
            usuario = Usuarios(nombre=usuario_nombre, apellido=usuario_apellido, email=usuario_email, profesion=usuario_profesion)
            usuario.save()
            return redirect(reverse_lazy('usuarios'))
    else:
        miForm = UsuariosForm()
    return render(request, "aplicacion/usuariosForm.html", {"form": miForm})


def buscar(request):
    return render(request, "aplicacion/buscar.html" )

def buscarInstrumentos(request):
    buscar_parametro = request.GET.get("buscar", None)
    if buscar_parametro:
        instrumentos = Instrumentos.objects.filter(descripcion__icontains=buscar_parametro)
        contexto = {"instrumentos": instrumentos}
        return render(request, "aplicacion/instrumentos.html", contexto)
    
    return redirect(reverse_lazy('instrumentos'))
