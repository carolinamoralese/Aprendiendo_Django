from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import HttpResponse, JsonResponse, Http404
from django.utils.text import slugify

# Create your views here.
class Clase1(APIView):
    

    def get(self, request):
        ...