from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import HttpResponse, JsonResponse, Http404
from http import HTTPStatus
from .models import *

class Clase1(APIView):
    
    
    def post(self, request):
        ...

# Create your views here.
