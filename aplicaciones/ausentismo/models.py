from django.db import models
from django.utils.timezone import now

from aplicaciones.core.models import Base, Pais, Provincia, Ciudad
from proyecto_administrativo import settings
from proyecto_administrativo.constantes import Opciones
opciones = Opciones()
GENERO = opciones.genero()
MOTIVO_PERMISO=opciones.motivo_permiso()

class Empleado(Base):
    nombres = models.CharField(max_length=200, unique=True)
    cedula = models.CharField(max_length=10, unique=True)
    #motivo_per=models.CharField(max_length=1,choices=MOTIVO_PERMISO,default=MOTIVO_PERMISO[0][0], blank=True, null=True)
    cargo = models.CharField(max_length=30)
    telefonos = models.CharField(max_length=10, blank=True, null=True)
    #dias_per=models.CharField(max_length=2, unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, blank=True, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True, verbose_name='Dirección')
    genero = models.CharField(max_length=1, choices=GENERO,default=GENERO[0][0], blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=100,unique=True)
    foto = models.FileField(upload_to='ausentismos/empleados/', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nombres)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ('nombres',)

    def get_image(self):
        if self.foto:
            return '{}{}'.format(settings.MEDIA_URL, self.foto)
        return '{}{}'.format(settings.STATIC_URL, 'img/default/empty.jpg')

class Permiso(Base):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT,null=True,blank=True)
    cedula = models.CharField(max_length=10, unique=True)
    cargo = models.CharField(max_length=30)
    telefonos = models.CharField(max_length=10, blank=True, null=True)
    motivo_permiso = models.CharField(max_length=10, choices=MOTIVO_PERMISO, default=MOTIVO_PERMISO[0][0], blank=True, null=True)
    fecha_permiso = models.DateField(default=now)
    dias_permiso=models.CharField(max_length=2, unique=True)
    periodo=models.DateField(default=now)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {}".format(self.id, self.empleado, self.empleado.cedula, self.empleado.cargo, self.empleado.telefonos, self.motivo_permiso)

    class Meta:
        verbose_name = "Permiso"
        verbose_name_plural = "Permisos"
        ordering = ('motivo_permiso', 'empleado')

class PermisoVacaciones(Base):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    cedula = models.CharField(max_length=10, unique=True)
    cargo = models.CharField(max_length=30)
    telefonos = models.CharField(max_length=10, blank=True, null=True)
    permiso=models.CharField(max_length=10,default="Vacaciones", )
    fecha_salida=models.DateTimeField(default=now)
    fecha_reintegro=models.DateField(default=now)
    dias_permiso=models.CharField(max_length=2,default="30")
    periodo=models.DateField(default=now)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {}".format(self.id, self.empleado, self.empleado.cedula, self.empleado.cargo, self.empleado.telefonos, self.permiso, self.fecha_reintegro)

    class Meta:
        verbose_name = "Permiso Vacaciones"
        verbose_name_plural = "Permiso por Vacaciones"
        ordering = ('empleado',)


