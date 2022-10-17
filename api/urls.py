from django.urls import path, include

app_name = 'api'

urlpatterns = [

]

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
