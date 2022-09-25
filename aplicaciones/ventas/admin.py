from django.contrib import admin
from django.contrib.admin import AdminSite
from aplicaciones.ventas.models import Cliente, Articulo,FacturaDetalle,Factura

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('ruc','nombres','ciudad','direccion','estado',)
    ordering = ('nombres',)
    search_fields = ('ruc', 'nombres',)
    list_filter = ('ciudad__nombre','estado', )
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Articulo)

class FacturaDetalleDetailsInline(admin.TabularInline):
    model = FacturaDetalle
    extra = 0

class FacturaAdmin(admin.ModelAdmin):
    inlines = (FacturaDetalleDetailsInline, )
    list_display = ('cliente','forma_pago','fecha','subtotal','iva','total','estado', )
    list_per_page = 20
    ordering = ('-fecha',)
    search_fields = ('fecha', 'cliente__nombres')
    list_filter = ('fecha','estado')

admin.site.register(Factura,FacturaAdmin)

