from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.response import Response
from http import HTTPStatus
from django.core.files.storage import FileSystemStorage
import os
from datetime import datetime

# Create your views here.
class Class_Ejemplo(APIView):
    def get(self, request):
        #return Response({"estado": "ok", "mensaje": f"metodo GET | id={request.GET.get('id', None)} | slug={request.GET.get('slug')}"})
       return JsonResponse({
            "estado": "ok",
            "mensaje": f"metodo GET | id={request.GET.get('id', None)} | slug={request.GET.get('slug')}"
        }, status=HTTPStatus.ok)
    
    def post(self, request):
        if request.data.get("correo") == None or request.data.get("password") == None:
            raise Http404
        return JsonResponse({ "estado": "ok", "mensaje": f"metodo POST | correo={request.data.get('correo')} | password={request.data.get("password")}"},status=HTTPStatus.CREATED)
    


class Class_EjemploParamentros(APIView):
    def get(self, request, id):
       return JsonResponse({"mensaje": f"metodo GET | parametros={id}"},stauts=HTTPStatus.FOUND)
    

    def put(self, request, id):
        return JsonResponse({"mensaje": f"metodo PUT | parametros={id}"})

    def delete(self, request, id):
       return JsonResponse({"mensaje": f"metodo DELETE | parametros={id}"})
    

class Class_EjemploUpload(APIView):

    def post(self, request):
        fs = FileSystemStorage()

        archivo = request.FILES["file"]
        fecha = datetime.now()
        foto = f"{datetime.timestamp(fecha)}{os.path.splitext(str(request.FILES['file']))[1]}"

        nombre = fs.save(f"ejemplo/{foto}", archivo)
        url = fs.url(nombre)

        return JsonResponse({
            "estado": "ok",
            "mensaje": "se subió el archivo",
            "url": url
        })