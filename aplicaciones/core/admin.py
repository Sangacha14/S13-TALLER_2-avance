from django.contrib import admin

from aplicaciones.core.models import Linea, Grupo,Pais,Provincia,Ciudad,Empresa

admin.site.register(Linea)
admin.site.register(Grupo)
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(Empresa)
