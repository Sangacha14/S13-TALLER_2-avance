from django.db import models
from django.utils.timezone import now

from aplicaciones.core.models import Base, Pais, Provincia, Ciudad, Grupo, Linea
from proyecto_administrativo import settings
from proyecto_administrativo.constantes import Opciones
opciones = Opciones()
FORMA_PAGO=opciones.forma_pago()
GENERO = opciones.genero()

class Cliente(Base):
    ruc = models.CharField(max_length=13, unique=True)
    nombres = models.CharField(max_length=200, unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, blank=True, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True, verbose_name='Dirección')
    genero = models.CharField(max_length=1, choices=GENERO,default=GENERO[0][0], blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    telefonos = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100,unique=True)
    foto = models.FileField(upload_to='ventas/clientes/', blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.nombres)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ('nombres',)

    def get_image(self):
        if self.foto:
            return '{}{}'.format(settings.MEDIA_URL, self.foto)
        return '{}{}'.format(settings.STATIC_URL, 'img/default/empty.jpg')

class Articulo(Base):
    descripcion = models.CharField(verbose_name='Descripcion',max_length=100,unique=True)
    alias = models.CharField(verbose_name='Alias',max_length=100,unique=True)
    codigo_barra = models.CharField(max_length=20, blank=True, null=True,unique=True)
    stock_minimo = models.FloatField(default=0)
    stock_maximo = models.FloatField(default=0)
    foto = models.FileField(upload_to='ventas/articulos/', null=True, blank=True)
    linea = models.ForeignKey(Linea, on_delete=models.PROTECT,null=True, blank=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT,null=True, blank=True)
    stock = models.IntegerField('Stock',default=0)
    costo = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de Costo')
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de Venta')
    con_iva = models.BooleanField("Iva",default=True)
    estado = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['descripcion']
    def __str__(self):
        return self.descripcion


class Factura(Base):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT,null=True,blank=True)
    forma_pago = models.CharField(max_length=1,choices=FORMA_PAGO,default=FORMA_PAGO[0][0])
    fecha = models.DateField(default=now)
    subtotal = models.DecimalField(default=0, max_digits=16, decimal_places=2)
    iva = models.DecimalField(default=0, max_digits=16, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=16, decimal_places=2)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {} ({})".format(self.id, self.cliente, self.total)

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        ordering = ('-fecha', 'cliente')

    def formaPago(self):
        if self.forma_pago=="E":
           pago="Efectivo"
        elif self.forma_pago=="C":
            pago="Credito"
        else:
            pago="Paypal"
        return pago

class FacturaDetalle(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.PROTECT)
    articulo = models.ForeignKey(Articulo, on_delete=models.PROTECT)
    cantidad = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    precio = models.DecimalField(default=0, max_digits=16, decimal_places=2)
    subtotal = models.DecimalField(default=0, max_digits=16, decimal_places=2)
    tasa_iva = models.FloatField(default=0, null=True, blank=True)
    iva = models.DecimalField(default=0, max_digits=16, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=16, decimal_places=2)

    def __str__(self):
        return "{} - {}".format(self.articulo, self.cantidad)

    class Meta:
        verbose_name = "Factura Detalle"
        verbose_name_plural = "Factura Detalles"
        ordering = ('factura',)

