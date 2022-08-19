from rest_framework import serializers
from models import models

class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Collection
        fields = '__all__'

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mark
        fields = '__all__'

class URL_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.URL
        fields = '__all__'

class IMAGE_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.IMAGE
        fields = '__all__'

class NOTE_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.NOTE
        fields = '__all__'