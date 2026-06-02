from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True) #texto corto, máximo 100 caracteres, unique=evitar duplicados
    descripcion = models.TextField(blank=True) #blank= se puede dejar en blanco el formulario
    def __str__(self):
        return self.nombre


class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    ingredientes = models.TextField()
    pasos = models.TextField()
    tiempo_preparacion = models.PositiveIntegerField(help_text="Tiempo en minutos")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='recetas') # muchas recetas pueden pertenecer a una categoría
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recetas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_creacion'] #ordena de mas nueva a mas antigua

    def __str__(self):
        return self.titulo

    def get_absolute_url(self): # devuelve la URL del detalle de la receta (usada por las vistas genéricas para redirigir después de crear/editar)
        return reverse('detalle_receta', kwargs={'pk': self.pk})


class Comentario(models.Model):
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='comentarios')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f'Comentario de {self.autor} en {self.receta}'

