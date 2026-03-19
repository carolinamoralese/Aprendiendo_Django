from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import HttpResponse, JsonResponse, Http404
from http import HTTPStatus
from .models import Contacto
from datetime import datetime

from utilidades import utilidades


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

        try:
            Contacto.objects.create(nombre=request.data["nombre"], correo=request.data["correo"], telefono=request.data["telefono"], mensaje=request.data["mensaje"], fecha=datetime.now())

            html=f"""
                <h1>Nuevo mensaje en contacto</h1>
                <ul>
                    <li>Nombre: {request.data['nombre']}</li>
                    <li>correo: {request.data['correo']}</li>
                    <li>telefono: {request.data['telefono']}</li>
                    <li>mensaje: {request.data['mensaje']}</li>
                </ul>
            """
            utilidades.sendMail(html, "prueba envio de correo", request.data['correo'])
        except Exception as e:
            return JsonResponse({"estado": "error", "mensaje": "Ocurrios un error inesperado"}, status=HTTPStatus.BAD_REQUEST)
           
        return JsonResponse({"estado": "ok", "mensaje": "Se crea registro exitosamente"}, status=HTTPStatus.OK)