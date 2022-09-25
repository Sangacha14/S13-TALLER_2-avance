from django.urls import path

from .views.cliente.views import ClienteListView, CrearCliente, ActualizarCliente, EliminarCliente
from .views.menu.views import MenuTemplateView
from .views.venta.views import ConsultaVenta, CrearVenta, EditarVenta

app_name = "ventas"
urlpatterns = [
    # cliente
    path('cliente', ClienteListView.as_view(), name='cliente'),
    path('crearcliente/', CrearCliente.as_view(), name='crearcliente'),
    path('actualizarcliente/<int:pk>/', ActualizarCliente.as_view(), name='actualizarcliente'),
    path('eliminarcliente/<int:pk>/', EliminarCliente.as_view(), name='deletecliente'),
    # ventas
    path('menu', MenuTemplateView.as_view(), name="menu"),
    path('consulta/', ConsultaVenta.as_view(), name='consultaventa'),
    path('crear/', CrearVenta.as_view(), name='crearventa'),
    path('editar/<int:pk>/', EditarVenta.as_view(), name='editarventa'),
]
