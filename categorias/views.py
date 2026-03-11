from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from django.http.response import HttpResponse, JsonResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from http import HTTPStatus
from django.utils.text import slugify

# Create your views here.
class Clase1(APIView):


    def get(self, request):
        #select * from irder by id desc
        data = Categoria.objects.order_by('-id').all() #nombre del modelo.objects.order_by('-id')
        datos_json = CategoriaSerializer(data, many=True)
        #return Response(datos_json.data)
        return JsonResponse({"data": datos_json.data},status=HTTPStatus.OK)
    

    def post(self, request):
        if request.data.get("nombre")== None or not request.data["nombre"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo nombre es obligatorio"}, status= HTTPStatus.BAD_REQUEST)
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


    def put(self, request, id):
        if request.data.get("nombre")== None or not request.data["nombre"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo nombre es obligatorio"}, status= HTTPStatus.BAD_REQUEST)
        try:
            data = Categoria.objects.filter(pk=id).get()
            Categoria.objects.filter(pk=id).update(nombre=request.data.get("nombre"), slug=slugify(request.data.get("nombre")))
            return JsonResponse({"estado":"ok", "mensaje": "Se modifica el registro exitosamente"}, status= HTTPStatus.ok)
        except Categoria.DoesNotExist:
            raise Http404
        

    def delete(self, request, id):
        try:
            data = Categoria.objects.filter(pk=id).get()
            Categoria.objects.filter(pk=id).delete()
            return JsonResponse({"estado":"ok", "mensaje": "Se elimina el registro exitosamente"}, status= HTTPStatus.ok)
        except Categoria.DoesNotExist:
            raise Http404