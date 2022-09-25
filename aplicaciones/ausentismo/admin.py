from django.contrib import admin
from django.contrib.admin import AdminSite
from aplicaciones.ausentismo.models import Empleado, Permiso, PermisoVacaciones


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombres', 'cargo', 'ciudad',)
    ordering = ('nombres',)
    search_fields = ('cedula', 'nombres',)
    list_filter = ('ciudad__nombre', 'cargo',)


admin.site.register(Empleado, EmpleadoAdmin)


# admin.site.register(Permiso)
# admin.site.register(PermisoVacaciones)

class PermisoAdmin(admin.ModelAdmin):
    # list_display = ('cedula', 'empleado','fecha_permiso','cargo', 'motivo_permiso','estado',)

    list_display = ('empleado', 'cedula', 'fecha_permiso', 'motivo_permiso',)
    list_per_page = 10
    ordering = ('empleado',)
    search_fields = ('motivo_permiso', 'empleado',)
    list_filter = ('motivo_permiso',)


admin.site.register(Permiso, PermisoAdmin)


class PermisoVacacionesAdmin(admin.ModelAdmin):
    # list_display = ('cedula','empleado','fecha_salida','cargo','permiso','estado')
    list_display = ('empleado', 'fecha_reintegro', 'permiso',)
    list_per_page = 10
    ordering = ('empleado',)
    search_fields = ('empleado',)
    list_filter = ('fecha_reintegro',)


admin.site.register(PermisoVacaciones, PermisoVacacionesAdmin)
