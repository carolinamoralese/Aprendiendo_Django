from django.urls import path
from .views import Class_Ejemplo, Class_EjemploParamentros

urlpatterns = [
    path('ejemplo', Class_Ejemplo.as_view()),
    path('ejemplo/<int:id>', Class_EjemploParamentros.as_view())
]
