from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

"""Una vista basada en una clase es una clase que actúa como una función de la vista. 
Como es una clase, se pueden crear diferentes instancias de la clase con diferentes argumentos, para cambiar el comportamiento de la vista.
Esto también se conoce como vistas genéricas, reutilizables o enchufables."""
# ************ View **************
# Todas las vistas basadas en clases heredan de ella.
# Maneja las conexiones de la vista y las URLs.
# Metodos que se ejecutan en secuencia en las VBC - View(su uso con token)
#1. dispatch(): valida la peticion(metodo http post/get) si no encuentra el metodo paso 2
#2. http_method_not_allowed(): retorna un error cuando se utiliza un metod http
# no soportado o definido
#3. options(): es opcional se lo utiliza para soportar otros metodos http


# def inicio(request):
#        print(request)
#        if request.method == 'GET':
#               return render(request, "base.html",{'titulo':"Menu Inicio",'url_anterior':"/"})
#        else:
#            pass
# class InicioView(View):
#
#     def get(self,request,*args,**kwargs):
#         print(request)
#         return render(request,'base.html',{'titulo':"Menu Principal",'url_anterior':"/"})
# class TemplateView(View):
#     template_name=""
#     extrax_context="object_list"
#     def get_context_data(self, **kwargs):
#         context = {"url":"inicio/","user":""}
#         return context
#
#     def get(self,request,*args,**kwargs):
#          print(request)
#          return render(request,self.template_name,{'titulo':"Menu Principal",'url_anterior':"/"})

class InicioTemplateView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Menu Principal"
        context['url_anterior']= '/'
        return context