from django.contrib import admin

from .models import *  


# Register your models here.

admin.site.register(Tipos)
admin.site.register(Usuarios)
admin.site.register(Instrumentos)
admin.site.register(Operaciones)
admin.site.register(Cuentas)