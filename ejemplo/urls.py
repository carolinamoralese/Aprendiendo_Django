from django.urls import path
from .views import Class_Ejemplo, Class_EjemploParamentros, Class_EjemploUpload

urlpatterns = [
    path('ejemplo/', Class_Ejemplo.as_view()),
    path('ejemplo/<int:id>', Class_EjemploParamentros.as_view()),
    path('ejemplo-upload', Class_EjemploUpload.as_view())
]
