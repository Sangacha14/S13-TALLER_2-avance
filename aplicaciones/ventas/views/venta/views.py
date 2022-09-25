import json
from decimal import Decimal

from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from aplicaciones.ventas.forms import VentaForm
from aplicaciones.ventas.models import Factura, Articulo, FacturaDetalle
from proyecto_administrativo.constantes import Opciones


class ConsultaVenta(ListView):
    template_name = 'venta/list.html'
    context_object_name = 'facturas'
    model = Factura
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(cliente__nombres__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/venta/menu/'
        context['listar_url'] = '/venta/consulta/',
        context['crear_url'] = '/venta/crear/'
        context['titulo'] = 'LISTADO DE FACTURAS'
        context['query'] = self.request.GET.get("query") or ""
        return context


class CrearVenta(CreateView):
    template_name = 'venta/form_venta.html'
    model = Factura
    success_url = reverse_lazy('ventas:consultaventa')
    form_class = VentaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/venta/crear/'
        context['titulo'] = 'CREAR VENTA'
        context['url_anterior'] = '/venta/menu'
        context['listar_url'] = '/venta/consulta'
        context['action'] = 'add'
        context['articulos'] = Articulo.objects.filter(estado=True)
        context['iva'] = Opciones.iva
        return context

    def post(self, request, *args, **kwargs):
        resp = {}
        try:
            data = json.loads(request.body)
            if data['action'] == 'add':
                with transaction.atomic():
                    factura = Factura()
                    factura.usuario_id = request.user.id
                    factura.cliente_id = int(data['cliente'])
                    factura.fecha = data['fecha']
                    factura.forma_pago = data['forma_pago']
                    factura.subtotal = float(data['subtotal'])
                    factura.iva = float(data['iva'])
                    factura.total = float(data['total'])
                    factura.save()
                    items = data['articulos']
                    for item in items:
                        art = Articulo.objects.filter(id=int(item['id']))
                        if art.exists():
                            detalle = FacturaDetalle(
                                factura_id=factura.id,
                                articulo_id=int(item['id']),
                                cantidad=float(item['cantidad']),
                                precio=float(item['precio']),
                                subtotal=float(item['subtotal']),
                                iva=float(item['iva']),
                                total=float(item['total'])
                            )
                            detalle.save()
                            articuloReal = art[0]
                            articuloReal.stock = articuloReal.stock - Decimal(detalle.cantidad)
                            articuloReal.save()
                            resp["grabar"] = "ok"
            else:
                pass
        except Exception as e:
            resp["grabar"] = str(e)
            print(e)

        return JsonResponse(resp, safe="false")


class EditarVenta(UpdateView):
    template_name = 'venta/form_venta.html'
    model = Factura
    success_url = reverse_lazy('ventas:consultaventa')
    form_class = VentaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = f'/venta/editar/{self.get_object().id}/'
        context['titulo'] = 'EDITAR VENTA'
        context['url_anterior'] = '/venta/menu'
        context['listar_url'] = '/venta/consulta'
        context['action'] = 'edit'
        context['articulos'] = Articulo.objects.filter(estado=True)
        context['iva'] = Opciones.iva
        context['detalle'] = json.dumps(self.get_detalle_factura())
        return context

    def get_detalle_factura(self):
        detalle = []
        try:

            for det in FacturaDetalle.objects.filter(factura_id=self.get_object().id):
                item = {}
                item['id'] = det.articulo_id
                item['descripcion'] = det.articulo.descripcion
                item['cantidad'] = str(det.cantidad)
                item['precio'] = str(det.precio)
                item['subtotal'] = str(det.subtotal)
                item['iva'] = str(det.iva)
                item['total'] = str(det.total)
                detalle.append(item)
        except:
            pass
        return detalle

    def post(self, request, *args, **kwargs):
        resp = {}
        try:
            data = json.loads(request.body)
            if data['action'] == 'edit':
                with transaction.atomic():
                    # factura = Factura.objects.get(id=self.get_object().id)
                    factura = self.get_object()
                    factura.usuario_id = request.user.id
                    factura.cliente_id = int(data['cliente'])
                    factura.fecha = data['fecha']
                    factura.forma_pago = data['forma_pago']
                    factura.subtotal = float(data['subtotal'])
                    factura.iva = float(data['iva'])
                    factura.total = float(data['total'])
                    factura.save()
                    # for det in factura.facturadetalle_set.all():
                    #     det.delete()

                    factura.facturadetalle_set.all().delete()
                    items = data['articulos']
                    for item in items:
                        art = Articulo.objects.filter(id=int(item['id']))
                        if art.exists():
                            detalle = FacturaDetalle(
                                factura_id=factura.id,
                                articulo_id=int(item['id']),
                                cantidad=float(item['cantidad']),
                                precio=float(item['precio']),
                                subtotal=float(item['subtotal']),
                                iva=float(item['iva']),
                                total=float(item['total'])
                            )
                            detalle.save()
                            articuloReal = art[0]
                            articuloReal.stock = articuloReal.stock - Decimal(detalle.cantidad)
                            articuloReal.save()
                            resp["grabar"] = "ok"
            else:
                pass
        except Exception as e:
            resp["grabar"] = str(e)
            print(e)

        return JsonResponse(resp, safe="false")
