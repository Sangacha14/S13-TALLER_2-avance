
from proyecto_administrativo.wsgi import get_wsgi_application
from aplicaciones.ventas.models import Cliente
#from django.db.models import Q, Avg,Sum,Count
#from aplicaciones.core.models import Linea,Grupo
print("python")
# from django.contrib.auth.models import User
#print(User.objects.all())
# mostrar todos los registros
# Insertar registros con create()
#Linea.objects.create(descripcion="Rio Store")
#Linea.objects.create(descripcion="Mi Comisariato")

# Insertar registros con intancias del modelo
"""p = Linea()
p.descripcion="Mi Jugueteria"
p.save()
p=Linea(descripcion="Panaderia")
p.save()
Linea(descripcion="Perfumeria").save()"""
# Actualizar - Modificar - Editar un registro
"""p = Linea.objects.get(id=6)
p.descripcion="Jugueteria"
p.save()
p = Linea.objects.get(descripcion="Panaderia")
p.descripcion="Mi Panaderia"
p.save()"""
# Grabar modelo relacionado
"""lin= Linea.objects.get(id=7)
grupo=Grupo(descripcion="Embutidos4",linea=lin)
grupo.save()"""
#Grupo.objects.create(descripcion="Embutidos5",linea_id=7)
#print(Grupo.objects.all())
# Eliminar registros
"""try:
    p = Linea.objects.get(id=10)
    p.delete()
    print("Registro borrado")
except Exception as e:
    print("Error --> ",e)
print(Linea.objects.values("id"))
print(Linea.objects.all())
"""
# Consultar registro con get (un solo registro)
"""print(Linea.objects.all())
print(Linea.objects.all().query)
print(Linea.objects.all().values('id'))
print(list(Linea.objects.values()))
linea = list(Linea.objects.all().values())
print(linea)
# Recorrer consulta - query
for p in linea:
    print(p['id'], p['descripcion'])
"""
# Consultar registros con filter (varios registros segun la condicion)
"""linea = Linea.objects.filter(id=7)
linea = Linea.objects.filter(id__gt=7).values("id","descripcion")
linea = Linea.objects.filter(id__gte=7).values("id","descripcion")
linea = Linea.objects.filter(id__lt=7).values("id","descripcion")
linea = Linea.objects.filter(id__lte=7).values("id","descripcion")
linea = Linea.objects.filter(descripcion__contains="p").values("id","descripcion")
linea = Linea.objects.filter(id__in=[4,6,8]).values("id","descripcion")
print(linea)"""
#Queries Q
# o (or)
#linea=Linea.objects.filter(Q(id=4)|Q(id=5)).values("id","descripcion")
# y and
#linea=Linea.objects.filter(Q(descripcion__istartswith="Mi") & Q(descripcion__iendswith="to")).values("id","descripcion")
# exclude
#linea=Linea.objects.exclude(Q(descripcion__istartswith="Mi") & Q(descripcion__iendswith="to")).values("id","descripcion")
#print(linea)
#linea = Linea.objects.exclude(id=7).values("id","descripcion")
# consulta con modelos relacionados del hijo al padre
"""grupo = Grupo.objects.filter(linea__descripcion__icontains="Rio").values()
grupo = Grupo.objects.filter(linea__descripcion__icontains="Rio")"""
#grupo = Grupo.objects.all().values()
#print(grupo)
#for g in grupo:
  #print(g['id'],g['linea_id'],g['descripcion'])
  #print(g)
  #print(g.linea.descripcion,g.id,g.descripcion)
# Relaciones inversa
#print(Linea.objects.get(id=4).grupo_set.filter(id__gte=7))
# del padre al hijo
#print(Linea.objects.get(id=4).grupos.filter(id__gte=7))
#lin = Linea.objects.get(id=4)
#print(lin.grupos.filter(id__gte=7))
# del hijo al padre
#print(Grupo.objects.filter(id__gte=7,linea__id=4))
#print(Grupo.objects.filter(linea__descripcion__icontains="Mi").query)
# agregaciones
#valor = Linea.objects.filter(id__lt=6).aggregate(suma=Sum('id'))
#print(valor,valor['suma'])
"""print(Linea.objects.values("id","estado"))
Linea.objects.filter(id__in=[4,5]).update(estado=True)
print(Linea.objects.values("id","estado"))
"""
# gru1 = Grupo.objects.filter(id__in=[4,6,8]).select_related('linea')
# gru2 = Grupo.objects.filter(id__in=[4,6,8])
# for g in gru1:
#        print(g.id,g.linea.descripcion)
#
# print(gru2)
#print(Linea.objects.get(id=4).grupos.filter(id__gte=7))
from weasyprint import HTML
from django.template.loader import get_template

def impresion():
    template= get_template("factur.html")
    clientes = get_clientes()
    context={"titulo":"LISTADO DE CLIENTES","clientes":clientes}
    html_template = template.render(context)
    HTML(string=html_template).write_pdf(target="clientes.pdf")

def get_clientes():
    clientes = Cliente.objects.all()
    return clientes
impresion()