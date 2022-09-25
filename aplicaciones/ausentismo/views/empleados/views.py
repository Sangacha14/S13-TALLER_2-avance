from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from aplicaciones.ausentismo.formulario import PermisoFormulario
from aplicaciones.ausentismo.models import Empleado, Permiso, PermisoVacaciones


class EmpleadoListView(ListView):
    template_name = "empleado/lista.html"
    model = Empleado
    context_object_name = 'empleados'
    paginate_by = 5
    #queryset = Cliente.objects.filter(estado=True)

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(nombres__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/ausentismo/menu'
        context['listar_url']= '/ausentismo/empleado/'
        context['crear_url'] = '/ausentismo/crearempleado/'
        context['titulo'] = 'LISTADO DE EMPLEADOS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearEmpleado(CreateView):
    model = Empleado
    template_name = "empleado/error.html"
    success_url = reverse_lazy('ausentismo:empleado')
    form_class = Empleado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/ausentismo/crearempleado/'
        context['titulo'] = 'CREAR EMPLEADO'
        context['url_anterior'] = '/ausentismo/empleado/'
        context['listar_url'] = '/ausentismo/empleado/'
        context['action'] = 'add'
        return context

# class ActualizarCliente(UpdateView):
#     model = Cliente
#     template_name = "cliente/form.html"
#     success_url = reverse_lazy('ventas:cliente')
#     form_class = ClienteForm
#     #queryset = Cliente.objects.get(pk=request.GET.get("id"))
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['action_save'] = self.request.path
#         context['titulo'] = 'ACTUALIZAR DE CLIENTE'
#         context['url_anterior'] = '/venta/cliente'
#         context['listar_url'] = '/venta/cliente'
#         return context
#
#
# class EliminarCliente(DeleteView):
#     model = Cliente
#     template_name = "cliente/delete.html"
#     success_url = reverse_lazy('ventas:cliente')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['action_save'] = self.request.path
#         context['titulo'] = 'ELMINAR DE CLIENTE'
#         context['url_anterior'] = '/venta/cliente'
#         context['listar_url'] = '/venta/cliente'
#         return context
#
#
