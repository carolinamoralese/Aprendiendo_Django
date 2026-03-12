from rest_framework import serializers
from .models import *

# deberia tener nombre del modelo y sunfijo serializer
class RecetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receta
        #fields = ("id", "nombre", "slug")
        fields= '__all__'