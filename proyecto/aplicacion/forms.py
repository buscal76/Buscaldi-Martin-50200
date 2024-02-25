from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#__________________________________________________________________________Tipos
class TipoForm(forms.Form):
    tipo = forms.CharField(max_length=40, required=True)
    renta = forms.CharField(max_length=20, required=True)

#__________________________________________________________________________Operaciones
class OperacionesForm(forms.Form):
    tipo = forms.CharField(max_length=15, required=True)
    cuenta = forms.IntegerField(required=True)
    nominales = forms.IntegerField(required=True)
    ticker = forms.CharField(max_length=6, required=True)
    fecha = forms.DateField()

#__________________________________________________________________________Instrumentos
class InstrumentosForm(forms.Form):
    ticker = forms.CharField(max_length=6, required=True)
    tipo =  forms.CharField(max_length=40, required=True)
    descripcion = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)

#__________________________________________________________________________Cuentas
class CuentasForm(forms.Form):
    cuenta_comitente = forms.IntegerField(required=True)
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    apertura = forms.DateField()
    email = forms.EmailField(required=True)

#__________________________________________________________________________Registro Usuario
class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name', 'password1', 'password2']

#__________________________________________________________________________Edit Usuario    
class UserEditForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

#__________________________________________________________________________Avatar  
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)