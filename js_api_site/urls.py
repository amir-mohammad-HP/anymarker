from django.urls import path
from js_api_site.views import Collection

app_name = 'js_api_site'

urlpatterns = [
    path('', Collection.as_view(), name = 'collection'),
]
