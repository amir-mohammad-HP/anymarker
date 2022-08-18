from rest_framework import viewsets
from rest_framework import permissions
from models import models
from api.serializers import CollectionSerializer

class CollectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows collection to be viewed or edited.
    """
    queryset = models.Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]
    

