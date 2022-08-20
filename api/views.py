from rest_framework import viewsets
from rest_framework import permissions
from models import models
from api.serializers import CollectionSerializer, MarkSerializer, URL_Serializer, IMAGE_Serializer, NOTE_Serializer

class CollectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows collection to be viewed or edited.
    """
    queryset = models.Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user = self.request.user)
    
    
class MarkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Mark to be viewed or edited.
    """
    queryset = models.Mark.objects.all()
    serializer_class = MarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(collection__user = self.request.user).order_by('-collection')

class URL_ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Mark to be viewed or edited.
    """
    queryset = models.URL.objects.all()
    serializer_class = URL_Serializer
    lookup_field = 'mark'
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(
            mark__collection__user = self.request.user,
            )
    
class IMAGE_ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Mark to be viewed or edited.
    """
    queryset = models.IMAGE.objects.all()
    serializer_class = IMAGE_Serializer
    lookup_field = 'mark'
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(
            mark__collection__user = self.request.user,
            )
    
class NOTE_ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Mark to be viewed or edited.
    """
    queryset = models.NOTE.objects.all()
    serializer_class = NOTE_Serializer
    lookup_field = 'mark'
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(
            mark__collection__user = self.request.user,
            )