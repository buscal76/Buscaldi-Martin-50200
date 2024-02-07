from django import forms

class TipoForm(forms.Form):
    tipo = forms.CharField(max_length=40, required=True)
    renta = forms.CharField(max_length=20, required=True)

class OperacionesForm(forms.Form):
    tipo = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    nominales = forms.IntegerField(required=True)
    ticker = forms.CharField(max_length=6, required=True)
    fecha = forms.DateField()

class InstrumentosForm(forms.Form):
    ticker = forms.CharField(max_length=6, required=True)
    tipo =  forms.CharField(max_length=6, required=True)
    descripcion = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)

class UsuariosForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    profesion = forms.CharField(max_length=50, required=True)