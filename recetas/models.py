from django.db import models
from autoslug import AutoSlugField
from categorias.models import Categoria

# Create your models here.
class Receta(models.Model):
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)#relaciono el model de uno a mucho
    nombre = models.CharField(max_length=100, null=False)
    slug = AutoSlugField(populate_from="nombre", max_length=100)
    tiempo = models.CharField(max_length=100, null=True)
    foto = models.CharField(max_length=100, null=True)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table='recetas'
        verbose_name='receta'
        verbose_name_plural='recetas'


