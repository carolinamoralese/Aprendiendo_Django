from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import HttpResponse, JsonResponse, Http404
from http import HTTPStatus
from django.utils.text import slugify
from .serializers import *
from .models import *

# Create your views here.
class Clase1(APIView):
    

    def get(self, request):
        data = Receta.objects.order_by('-id').all() #nombre del modelo.objects.order_by('-id')
        datos_json = RecetaSerializer(data, many=True)
        return JsonResponse({"data": datos_json.data},status=HTTPStatus.OK)