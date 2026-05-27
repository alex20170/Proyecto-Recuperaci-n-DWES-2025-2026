from django.urls import path
from .views import (
    ListaRecetasView,
    DetalleRecetaView,
    CrearRecetaView,
    EditarRecetaView,
    EliminarRecetaView,
    crear_comentario,
    eliminar_comentario,
)

urlpatterns = [
    path('', ListaRecetasView.as_view(), name='lista_recetas'),
    path('receta/<int:pk>/', DetalleRecetaView.as_view(), name='detalle_receta'),
    path('receta/nueva/', CrearRecetaView.as_view(), name='crear_receta'),
    path('receta/<int:pk>/editar/', EditarRecetaView.as_view(), name='editar_receta'),
    path('receta/<int:pk>/eliminar/', EliminarRecetaView.as_view(), name='eliminar_receta'),
    path('receta/<int:pk>/comentar/', crear_comentario, name='crear_comentario'),
    path('comentario/<int:pk>/eliminar/', eliminar_comentario, name='eliminar_comentario'),
]
