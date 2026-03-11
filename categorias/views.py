from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from django.http.response import HttpResponse, JsonResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from http import HTTPStatus

# Create your views here.
class Clase1(APIView):


    def get(self, request):
        #select * from irder by id desc
        data = Categoria.objects.order_by('-id').all() #nombre del modelo.objects.order_by('-id')
        datos_json = CategoriaSerializer(data, many=True)
        #return Response(datos_json.data)
        return JsonResponse({"data": datos_json.data},status=HTTPStatus.OK)
    

    def post(self, request):
        try:
            Categoria.objects.create(nombre=request.data['nombre'])
            return JsonResponse({"estado":"ok", "mensaje": "Se crea el registro exitosamente"}, status= HTTPStatus.CREATED)
        except Exception as e:
            raise Http404


class Clase2(APIView):


    def get(self, request, id):
        #select * from categorias where id = 4
        try:
            data= Categoria.objects.filter(pk=id).get()
            return JsonResponse({"data": {"id": data.id, "nombre":data.nombre, "slug": data.slug}}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404