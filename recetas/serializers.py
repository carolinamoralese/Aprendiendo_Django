from rest_framework import serializers
from .models import *

# deberia tener nombre del modelo y sunfijo serializer
class RecetaSerializer(serializers.ModelSerializer):

    categoria = serializers.ReadOnlyField(source="categoria.nombre")# readonlyfiled pone el nombre de la categoria en lugar del id
    #categoria = serializers.ChartField(source="categoria.nombre")
    fecha = serializers.DateTimeField(format="%d/%m/%y")

    class Meta:
        model = Receta
        fields = ("id", "nombre", "slug", "tiempo", "descripcion", "fecha", "categoria", "categoria_id")
        #fields= '__all__'