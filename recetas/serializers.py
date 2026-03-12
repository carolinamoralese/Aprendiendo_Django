from rest_framework import serializers
from .models import *
from dotenv import load_dotenv
import os

# deberia tener nombre del modelo y sunfijo serializer
class RecetaSerializer(serializers.ModelSerializer):

    categoria = serializers.ReadOnlyField(source="categoria.nombre")# readonlyfiled pone el nombre de la categoria en lugar del id
    #categoria = serializers.ChartField(source="categoria.nombre")
    fecha = serializers.DateTimeField(format="%d/%m/%y")
    imagen = serializers.SerializerMethodField()# el nombre del campo debe ser igual al metodo get_nombreDelCampo

    class Meta:
        model = Receta
        fields = ("id", "nombre", "slug", "tiempo", "descripcion", "fecha", "categoria", "categoria_id", "imagen")
        #fields= '__all__'

    
    def get_imagen(self, obj):
        return f"{os.getenv('BASE_URL')}uploads/recetas/{obj.foto}"