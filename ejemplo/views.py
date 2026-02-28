from rest_framework.views import APIView
from django.http import HttpResponse

# Create your views here.
class Class_Ejemplo(APIView):
    def get(self, request):
        return HttpResponse(f"metodo GET | id={request.GET.get('id', None)} | slug={request.GET.get("slug")}")
    
    def post(self, request):
        return HttpResponse("metodo post")
    


class Class_EjemploParamentros(APIView):
    def get(self, request, id):
        return HttpResponse("metodo GET | parametros={id}".format(id))
    

    def put(self, request, id):
        return HttpResponse("metodo PUT | parametros={}".format(id))

    def delete(self, request, id):
        return HttpResponse("metodo DELETE | parametros={id}".format(id))