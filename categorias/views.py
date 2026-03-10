from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse, Http404
# Create your views here.
class Clase1(APIView):
    def get(self, request):
        pass