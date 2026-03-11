from rest_framework import serializers
from .models import *

# deberia tener nombre del modelo y sunfijo serializer
class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ("id", "nombre", "slug")
        #fields= '__all__'