from django.views.generic import TemplateView
from django.template.loader import render_to_string

# Create your views here.

class Collection(TemplateView):
    template_name = 'js_api_site/collection.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["template"] = {
            'profileView': render_to_string( template_name='js_api_site/inlineViews/profileView.html'),
        }
        return context
    