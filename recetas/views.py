from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import HttpResponse, JsonResponse, Http404
from http import HTTPStatus
from django.utils.text import slugify
from .serializers import *
from .models import *
from django.utils.dateformat import DateFormat
from dotenv import load_dotenv
import os


# Create your views here.
class Clase1(APIView):
    

    def get(self, request):
        data = Receta.objects.order_by('-id').all() #nombre del modelo.objects.order_by('-id')
        datos_json = RecetaSerializer(data, many=True)
        return JsonResponse({"data": datos_json.data},status=HTTPStatus.OK)

    
    def post(self, request):
        try:
            Receta.objects.create(nombre=request.data["nombre"], tiempo=request.data["tiempo"], descripcion=request.data["descripcion"], categoria_id = request.data['categoria'])
            return JsonResponse({"data": "ok", "mensaje":"se crea el registro existosamente"},status=HTTPStatus.CREATED)
        except Exception as e:
            raise Http404

class Clase2(APIView):


    def get(self, request, id):
        try:
            data = Receta.objects.filter(pk=id).get()
            return JsonResponse({"data" :{ "id": data.id, "nombre": data.nombre, "slug": data.slug, "tiempo": data.tiempo, "descripcion":data.descripcion, "fecha": DateFormat(data.fecha).format('d/m/Y'), "categoria_id": data.categoria_id, "categoria": data.categoria.nombre, "imagen": f"{os.getenv('BASE_URL')}uploads/recetas/{data.foto}"}}, status= HTTPStatus.OK)
        except Receta.DoesNotExist:
            return JsonResponse({"estado": "error", "mensaje":"Recurso no disponible"}, status=HTTPStatus.NOT_FOUND)