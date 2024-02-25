from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
 
#__________________________________________________________________________Home 
    path('', home, name="home"),

#__________________________________________________________________________Acerca de Mi
    path('acercademi/', acercademi, name="acercademi"),

#__________________________________________________________________________Instrumentos
    path('instrumentos/', InstrumentosList.as_view(), name="instrumentos"),
    path('instrumentos_create/', InstrumentosCreate.as_view(), name="instrumentos_create"),
    path('instrumentos_update/<int:pk>/', InstrumentosUpdate.as_view(), name="instrumentos_update"),
    path('instrumentos_delete/<int:pk>/', InstrumentosDelete.as_view(), name="instrumentos_delete"),

#__________________________________________________________________________Operaciones
    path('operaciones/', OperacionesList.as_view(), name="operaciones"),
    path('operaciones_create/', OperacionesCreate.as_view(), name="operaciones_create"),
    path('operaciones_update/<int:pk>/', OperacionesUpdate.as_view(), name="operaciones_update"),
    path('operaciones_delete/<int:pk>/', OperacionesDelete.as_view(), name="operaciones_delete"),

#__________________________________________________________________________Tipos
    path('tipos/', TiposList.as_view(), name="tipos"),
    path('tipos_create/', TiposCreate.as_view(), name="tipos_create"),
    path('tipos_update/<int:pk>/', TiposUpdate.as_view(), name="tipos_update"),
    path('tipos_delete/<int:pk>/', TiposDelete.as_view(), name="tipos_delete"),

#__________________________________________________________________________Cuentas
    path('cuentas/', CuentasList.as_view(), name="cuentas"),
    path('cuentas_create/', CuentasCreate.as_view(), name="cuentas_create"),
    path('cuentas_update/<int:pk>/', CuentasUpdate.as_view(), name="cuentas_update"),
    path('cuentas_delete/<int:pk>/', CuentasDelete.as_view(), name="cuentas_delete"),

#_________________________________________________________________________Loguin, Logout, Registration, Editar    
    path('login/', login_request, name="login"),
    path('registro/', register, name="registro"),
    path('logout/', custom_logout, name='logout'),
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
#__________________________________________________________________________Buscar    
    path('buscar/', views.buscar_instrumento, name='buscar_instrumento'),

]