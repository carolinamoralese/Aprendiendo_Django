from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import HttpResponse, JsonResponse, Http404
from http import HTTPStatus
from django.utils.text import slugify
from .serializers import *
from .models import *
from django.utils.dateformat import DateFormat
from django.core.files.storage import FileSystemStorage
from dotenv import load_dotenv
import os
from datetime import datetime


# Create your views here.
class Clase1(APIView):
    

    def get(self, request):
        data = Receta.objects.order_by('-id').all() #nombre del modelo.objects.order_by('-id')
        datos_json = RecetaSerializer(data, many=True)
        return JsonResponse({"data": datos_json.data},status=HTTPStatus.OK)

    
    def post(self, request):
        if not request.data.get('nombre'):
            return JsonResponse({"estado":"error", "mensaje":"El campo nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        if not request.data.get('tiempo'):
            return JsonResponse({"estado":"error", "mensaje":"El campo tiempo es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        if not request.data.get('descripcion'):
            return JsonResponse({"estado":"error", "mensaje":"El campo descripcion es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        if not request.data.get('categoria'):
            return JsonResponse({"estado":"error", "mensaje":"El campo categoria es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        #validamos que no exista la categoria id
        try:
            categoria = Categoria.objects.get(pk=request.data.get("categoria"))
        except Categoria.DoesNotExist:
            return JsonResponse(
                {"estado": "error", "mensaje": "La categoria no existe en la base de datos"},
                status=HTTPStatus.BAD_REQUEST)
        
        #validamos que el nombre no este duplicado
        if Receta.objects.filter(nombre=request.data.get("nombre")).exists():
            return JsonResponse({"estado":"error", "mensaje":f"El nombre {request.data["nombre"]} se encuentra creado ya"}, status=HTTPStatus.BAD_REQUEST)

        fs = FileSystemStorage()
        try:
            fecha = datetime.now()
            foto = f"{datetime.timestamp(fecha)}{os.path.splitext(str(request.FILES['foto']))[1]}"
        except Exception as e:
             return JsonResponse({"estado":"error", "mensaje":f"Debe adjuntar una foto para la receta"}, status=HTTPStatus.BAD_REQUEST)
        
        if request.FILES["foto"].content_type=="image/jpeg" or request.FILES["foto"].content_type=="image/png":
            try:
                archivo = request.FILES["foto"]
                foto = f"{datetime.timestamp(fecha)}{os.path.splitext(str(request.FILES['foto']))[1]}"
                nombre = fs.save(f"recetas/{foto}", archivo)
                url = fs.url(nombre)
            except Exception as e:
                return JsonResponse({"estado":"error", "mensaje":f"Se produjo un error al intentar subir el archivo"}, status=HTTPStatus.BAD_REQUEST)

            try:
                Receta.objects.create(
                    nombre=request.data["nombre"],
                    tiempo=request.data["tiempo"],
                    descripcion=request.data["descripcion"],
                    categoria_id=request.data["categoria"],
                    foto=foto
                )
                return JsonResponse({"data": "ok", "mensaje":"se crea el registro exitosamente"}, status=HTTPStatus.CREATED)

            except Exception as e:
                return JsonResponse({"estado":"error", "mensaje": str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
            
        return JsonResponse({"estado" : "error", "mensaje": "El formato debe ser jpeg o png"})

class Clase2(APIView):


    def get(self, request, id):
        try:
            data = Receta.objects.filter(pk=id).get()
            return JsonResponse({"data" :{ "id": data.id, "nombre": data.nombre, "slug": data.slug, "tiempo": data.tiempo, "descripcion":data.descripcion, "fecha": DateFormat(data.fecha).format('d/m/Y'), "categoria_id": data.categoria_id, "categoria": data.categoria.nombre, "imagen": f"{os.getenv('BASE_URL')}uploads/recetas/{data.foto}"}}, status= HTTPStatus.OK)
        except Receta.DoesNotExist:
            return JsonResponse({"estado": "error", "mensaje":"Recurso no disponible"}, status=HTTPStatus.NOT_FOUND)
        
    def put(self, request, id):
        try:
            data = Receta.objects.filter(pk=id).get()
        except Receta.DoesNotExist:
            return JsonResponse({"estado": "error", "mensaje":"Recurso no disponible"}, status=HTTPStatus.NOT_FOUND)
        
        if not request.data.get('nombre'):
            return JsonResponse({"estado":"error", "mensaje":"El campo nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        if not request.data.get('tiempo'):
            return JsonResponse({"estado":"error", "mensaje":"El campo tiempo es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        if not request.data.get('descripcion'):
            return JsonResponse({"estado":"error", "mensaje":"El campo descripcion es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        if not request.data.get('categoria'):
            return JsonResponse({"estado":"error", "mensaje":"El campo categoria es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        #validamos que no exista la categoria id
        try:
            categoria = Categoria.objects.get(pk=request.data.get("categoria"))
        except Categoria.DoesNotExist:
            return JsonResponse(
                {"estado": "error", "mensaje": "La categoria no existe en la base de datos"},
                status=HTTPStatus.BAD_REQUEST)

        try:
            Receta.objects.filter(pk=id).update( nombre=request.data["nombre"],
                    slug=slugify(request.data["nombre"]),
                    tiempo=request.data["tiempo"],
                    descripcion=request.data["descripcion"],
                    categoria_id=request.data["categoria"])
            return JsonResponse({"estado": "ok", "mensaje":"Se modifica el registro existoxamente"}, status=HTTPStatus.OK)
        except Exception as e:
             return JsonResponse({"estado": "error", "mensaje":"Ocurrio un error inesperado"}, status=HTTPStatus.NOT_FOUND)
        

    def delete(self, request, id):
        try:
            data = Receta.objects.get(pk=id)
        except Receta.DoesNotExist:
            return JsonResponse({"estado": "error", "mensaje":"Recurso no disponible"}, status=HTTPStatus.NOT_FOUND)

        # eliminar imagen si existe
        ruta = f"./uploads/recetas/{data.foto}"
        if os.path.exists(ruta):
            os.remove(ruta)

        # eliminar registro
        data.delete()

        return JsonResponse({"estado": "ok", "mensaje":"Receta eliminada"}, status=HTTPStatus.OK)
