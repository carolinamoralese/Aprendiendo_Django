from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import HttpResponse, JsonResponse, Http404
from http import HTTPStatus

# Create your views here.

class Clase1(APIView):

    def post(self, request):
        if request.data.get("nombre")== None or not request.data["nombre"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo nombre es obligatorio"}, status= HTTPStatus.BAD_REQUEST)
        if request.data.get("correo")== None or not request.data["correo"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo correo es obligatorio"}, status= HTTPStatus.BAD_REQUEST)
        if request.data.get("mensaje")== None or not request.data["mensaje"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo mensaje es obligatorio"}, status= HTTPStatus.BAD_REQUEST)
        if request.data.get("telefono")== None or not request.data["telefono"]:
            return JsonResponse({"estado": "error", "mensaje": "El campo telefono es obligatorio"}, status= HTTPStatus.BAD_REQUEST)