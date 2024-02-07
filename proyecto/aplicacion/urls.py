from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('instrumentos/', instrumentos, name="instrumentos"),
    path('tipos/', tipos, name="tipos"),
    path('usuarios/', usuarios, name="usuarios"),
    path('operaciones/', operaciones, name="operaciones"),
    #
    path('tipos_crear/', tiposForm, name="tiposCrear"),
    path('operaciones_crear/', operacionesForm, name="operacionesCrear"),
    path('instrumentos_crear/', instrumentosForm, name="instrumentosCrear"),
    path('usuarios_crear/', usuariosForm, name="usuariosCrear"),
    #
    path('buscar/', buscar, name="buscar"),
    path('buscarInstrumentos/', buscarInstrumentos, name="buscarInstrumentos"),
]
