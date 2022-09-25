from django.views.generic.base import TemplateView

class MenuTemplateView(TemplateView):
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Ventas"
        context['url_anterior'] = "/"
        return context

