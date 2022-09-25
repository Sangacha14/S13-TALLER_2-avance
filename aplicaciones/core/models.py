from django.contrib.auth.models import User
from django.db import models

class Base(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_modificacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    fecha_eliminacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    class Meta:
        abstract=True

class Pais(Base):

    nombre = models.CharField('Pais',max_length=50,unique=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.nombre)
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        ordering = ('nombre',)

class Provincia(Base):
    nombre = models.CharField('Provincia',max_length=50,unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.nombre)
    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        ordering = ('nombre',)

class Ciudad(Base):
    nombre = models.CharField(max_length=50,verbose_name='Ciudad',unique=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.nombre)
    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ('nombre',)

class Empresa(Base):
    ruc = models.CharField(max_length=13,unique=True)
    nombre = models.CharField(max_length=50,verbose_name='Empresa',unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, null=True, blank=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    latitud = models.CharField(max_length=70, blank=True, null=True)
    longitud = models.CharField(max_length=70, blank=True, null=True)
    responsable = models.CharField(max_length=50, blank=True, null=True)
    telefonos = models.CharField(max_length=50, blank=True, null=True)
    web = models.URLField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    logo = models.FileField(upload_to='logos/',blank=True, null=True)
    numero_sri = models.IntegerField(default=0)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.nombre)
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ('nombre',)

class Linea(Base):
    descripcion= models.CharField("Linea",max_length=100,unique=True,blank=True,null=True)
    imagen=models.FileField("Foto",upload_to="core/lineas",blank=True,null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Linea"
        verbose_name_plural = "Lineas"
        ordering = ('id',)
    def __str__(self):
        return "{}".format(self.descripcion)

class Grupo(Base):
    linea= models.ForeignKey(Linea,on_delete=models.PROTECT,null=True,blank=True,related_name="grupos")
    descripcion=models.CharField(verbose_name="Grupo",max_length=100,unique=True,blank=True,null=True)
    imagen = models.FileField("Foto", upload_to="core/Grupos", blank=True, null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        ordering = ('id',)
    def __str__(self):
        return "{} - {} - {}".format(self.linea.descripcion,self.id,self.descripcion)

