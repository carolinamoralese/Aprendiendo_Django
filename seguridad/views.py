from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from http import HTTPStatus
from .models import *
from django.contrib.auth.models import User
import uuid 
import os
from dotenv import load_dotenv
from utilidades import utilidades

class Clase1(APIView):
    
    
    def post(self, request):
        if request.data.get("nombre") == None or not request.data["nombre"]:
            return JsonResponse({"estado": "error", "mensaje": "campo nombre obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data["correo"] == None or not request.data["correo"]:
            return JsonResponse({"estado": "error", "mensaje": "campo correo obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data["password"] == None or not request.data["password"]:
            return JsonResponse({"estado": "error", "mensaje": "campo password obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        
        if User.objects.filter(email=request.data["correo"]).exists():
            return JsonResponse({"estado": "error", "mensaje": f"el correo ya se encuentra registrado"}, status=HTTPStatus.BAD_REQUEST)
        
        token = uuid.uuid4()
        url = f'{os.getenv("BASE_URL")}api/v1/seguridad/verificacion/{token}'

        try:
            user=User.objects.create_user(username=request.data["correo"], password=request.data["password"], email=request.data["correo"], first_name=request.data['nombre'], last_name="", is_active=0)
            UserMetaData.objects.create(token=token,user_id=user.id)

            html= f"""
            <h3>Verificacion de cuenta</h3>
            Hola {request.data["nombre"]} te haz registrado exitosamente. Para activar tu cuenta haz click en el siguiente enlace: <br/>
            <a href="{url}">{url}</a>
            """

            utilidades.sendMail(html, "Verificacion", request.data["correo"])
        except Exception as e:
            return JsonResponse({"estado": "error", "mensaje": "ocurrio un error inespertado"}, status=HTTPStatus.BAD_REQUEST)
        
        return JsonResponse({"estado": "ok", "mensaje": "se crea el registro exitosamente"}, status=HTTPStatus.CREATED)
    


class Clase2(APIView):
    
    def get(self, request, token):
        if token == None or not token:
              return JsonResponse({"estado": "error", "mensaje": "recurso no disponoble"}, status=404)
        
        try:
            data=UserMetaData.objects.filter(token=token).filter(user__is_active=0).get()
            
            UserMetaData.objects.filter(token=token).update(token="")

            User.objects.filter(id=data.user_id).update(is_active = 1)

            return HttpResponseRedirect(os.getenv("BASE_URL_FRONTEND"))
        except UserMetaData.DoesNotExist:
            raise Http404