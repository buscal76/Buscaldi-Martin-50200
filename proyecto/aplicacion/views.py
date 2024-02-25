from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from .models import * 
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms      import AuthenticationForm
from django.contrib.auth            import authenticate, login ,logout
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.db.models import Q

# Create your views here.

#__________________________________________________________________________Home
def home(request):
    return render(request, "aplicacion/home.html")

#__________________________________________________________________________Acerca de Mi
def acercademi(request):
    return render(request, "aplicacion/acercademi.html")


#__________________________________________________________________________Instrumentos
class InstrumentosList(LoginRequiredMixin, ListView):
    model = Instrumentos

class InstrumentosCreate(LoginRequiredMixin, CreateView):
    model = Instrumentos
    fields= ['ticker','tipo', 'descripcion', 'precio']
    success_url = reverse_lazy('instrumentos')

class InstrumentosUpdate(LoginRequiredMixin, UpdateView):
    model = Instrumentos
    fields = ['ticker','tipo', 'descripcion', 'precio']
    success_url = reverse_lazy('instrumentos')

class InstrumentosDelete(LoginRequiredMixin, DeleteView):
    model = Instrumentos
    success_url = reverse_lazy('instrumentos')

#_________________________________________________________________________Operaciones
class OperacionesList(LoginRequiredMixin, ListView):
    model = Operaciones

class OperacionesCreate(LoginRequiredMixin, CreateView):
    model = Operaciones
    fields= ['tipo', 'cuenta', 'nominales', 'ticker','fecha']
    success_url = reverse_lazy('operaciones')

class OperacionesUpdate(LoginRequiredMixin, UpdateView):
    model = Operaciones
    fields = ['tipo', 'cuenta', 'nominales', 'ticker','fecha']
    success_url = reverse_lazy('operaciones')

class OperacionesDelete(LoginRequiredMixin, DeleteView):
    model = Operaciones
    success_url = reverse_lazy('operaciones')

   
#__________________________________________________________________________Tipos
class TiposList(LoginRequiredMixin, ListView):
    model = Tipos

class TiposCreate(LoginRequiredMixin, CreateView):
    model = Tipos
    fields= ['tipo','renta']
    success_url = reverse_lazy('tipos')

class TiposUpdate(LoginRequiredMixin, UpdateView):
    model = Tipos
    fields = ['tipo','renta']
    success_url = reverse_lazy('tipos')

class TiposDelete(LoginRequiredMixin, DeleteView):
    model = Tipos
    success_url = reverse_lazy('tipos')

#__________________________________________________________________________Cuentas
class CuentasList(LoginRequiredMixin, ListView):
    model = Cuentas

class CuentasCreate(LoginRequiredMixin, CreateView):
    model = Cuentas
    fields= ['cuenta_comitente','nombre', 'apellido', 'apertura', 'email']
    success_url = reverse_lazy('cuentas')

class CuentasUpdate(LoginRequiredMixin, UpdateView):
    model = Cuentas
    fields = ['cuenta_comitente','nombre', 'apellido', 'apertura', 'email']
    success_url = reverse_lazy('cuentas')

class CuentasDelete(LoginRequiredMixin, DeleteView):
    model = Cuentas
    success_url = reverse_lazy('cuentas')

#__________________________________________________________________________Login, Logout, Registration
def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)

            #_________________________________________________________ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #_________________________________________________________


            return render(request, "aplicacion/home.html")
        else:
            return redirect(reverse_lazy('login'))
        
    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm })    


def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))

    else:    
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm })  

def custom_logout(request):
    logout(request)
    return redirect(reverse_lazy('home'))

#_________________________________________________________________________Edit Usuario
@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "aplicacion/home.html")
    else:    
        form = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": form }) 

#_________________________________________________________________________Avatar
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            # __________________________________
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___________ Hago una url de la imagen en request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "aplicacion/home.html")

    else:    
        form = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": form })     

#__________________________________________________________________________Buscar Instrumentos
@login_required
def buscar_instrumento(request):
    query = request.GET.get('q')

    if query:
        instrumentos = Instrumentos.objects.filter(descripcion__icontains=query)
    else:
        instrumentos = Instrumentos.objects.all()

    return render(request, 'aplicacion/resultado_busqueda.html', {'instrumentos': instrumentos, 'query': query})