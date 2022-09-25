from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from aplicaciones.ventas.forms import ClienteForm
from aplicaciones.ventas.models import Cliente

# class ClienteTemplateView(TemplateView):
#     template_name = "cliente/list.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['titulo'] = 'GESTION DE CLIENTES'
#         context['crear_url'] = '/venta/crearcliente'
#         context['listar_url'] = '/venta/cliente'
#         context['url_anterior'] = '/venta/menu'
#         return context

class ClienteListView(ListView):
    template_name = "cliente/list.html"
    model = Cliente
    context_object_name = 'clientes'
    paginate_by = 3
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
        context['url_anterior'] = '/venta/menu'
        context['listar_url']= '/cliente',
        context['crear_url'] = '/venta/crearcliente/'
        context['titulo'] = 'LISTADO DE CLIENTES'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearCliente(CreateView):
    model = Cliente
    template_name = "cliente/form.html"
    success_url = reverse_lazy('ventas:cliente')
    form_class = ClienteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/venta/crearcliente/'
        context['titulo'] = 'CREAR CLIENTE'
        context['url_anterior'] = '/venta/cliente'
        context['listar_url'] = '/venta/cliente'
        context['action'] = 'add'
        return context

class ActualizarCliente(UpdateView):
    model = Cliente
    template_name = "cliente/form.html"
    success_url = reverse_lazy('ventas:cliente')
    form_class = ClienteForm
    #queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR DE CLIENTE'
        context['url_anterior'] = '/venta/cliente'
        context['listar_url'] = '/venta/cliente'
        return context


class EliminarCliente(DeleteView):
    model = Cliente
    template_name = "cliente/delete.html"
    success_url = reverse_lazy('ventas:cliente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR DE CLIENTE'
        context['url_anterior'] = '/venta/cliente'
        context['listar_url'] = '/venta/cliente'
        return context



