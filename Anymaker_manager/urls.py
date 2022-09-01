"""Anymaker_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("favicon.png")),),
    path('', include('js_api_site.urls')),
    path('calls/', include('api.urls')),
    path("accounts/", include("authentification.urls")),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# rest framewwork
from rest_framework import serializers, viewsets, routers
from authentification.models import User
from api import views as api_views
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'collection', api_views.CollectionViewSet)
router.register(r'mark', api_views.MarkViewSet)
router.register(r'urls', api_views.URL_ViewSet)
router.register(r'images', api_views.IMAGE_ViewSet)
router.register(r'notes', api_views.NOTE_ViewSet)


urlpatterns += [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]