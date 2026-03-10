from django.urls import path
from .views import *

urlpatterns = [
    path('categoroas', Clase1.as_view())
]