from django.urls import path

#from .views.cliente.views import ClienteListView, CrearCliente, ActualizarCliente, EliminarCliente
from .views.empleados.views import EmpleadoListView
#from .views.menu.views import MenuTemplateView

from .views.menu.views import MenuTemplateView
#from .views.venta.views import ConsultaVenta, CrearVenta, EditarVenta
from .views.empleados.views import CrearEmpleado
app_name = "ausentismo"
urlpatterns = [
    ## MENU ausentimo
    path('menu/', MenuTemplateView.as_view(), name="menu"),

    ## EMPLEADOS
    path('empleado/',EmpleadoListView.as_view(),name='empleado'),
    path('crearempleado/',CrearEmpleado.as_view(),name='crearempleado'),

    ## PERMISO(PERSONAL-MEDICO)

    ## PERMISO VACACIONES


]


