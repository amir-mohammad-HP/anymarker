from re import template
from django.views.generic import TemplateView

# Create your views here.
class Collection(TemplateView):
    template_name = 'js_api_site/collection.html'