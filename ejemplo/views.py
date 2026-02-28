from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

# Create your views here.
class Class_Ejemplo(APIView):
    def get(self, request):
        #return Response({"estado": "ok", "mensaje": f"metodo GET | id={request.GET.get('id', None)} | slug={request.GET.get('slug')}"})
       return JsonResponse({
            "estado": "ok",
            "mensaje": f"metodo GET | id={request.GET.get('id', None)} | slug={request.GET.get('slug')}"
        })
    
    def post(self, request):
         return Response({
            "estado": "ok",
            "mensaje": f"metodo POST"
        })


class Class_EjemploParamentros(APIView):
    def get(self, request, id):
       return JsonResponse({"mensaje": f"metodo GET | parametros={id}"})
    

    def put(self, request, id):
        return JsonResponse({"mensaje": f"metodo PUT | parametros={id}"})

    def delete(self, request, id):
       return JsonResponse({"mensaje": f"metodo DELETE | parametros={id}"})