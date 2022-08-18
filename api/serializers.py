from rest_framework import serializers
from models import models

class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Collection
        fields = '__all__'