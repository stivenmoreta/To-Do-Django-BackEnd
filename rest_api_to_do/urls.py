from os import name
from django.urls import path
from .views import lista_tarea,eliminar_tarea,actualizar_tarea,actualizar_estado_tarea,agregar_tarea


urlpatterns = [
    path('lista_tarea/', lista_tarea, name="lista_tarea"), # http://127.0.0.1:8000/api/lista_tarea/
    path('eliminar_tarea/<id>', eliminar_tarea, name="eliminar_tarea"), # http://127.0.0.1:8000/api/eliminar_tarea/id
    path('actualizar_tarea/<id>', actualizar_tarea, name="actualizar_tarea"), # http://127.0.0.1:8000/api/actualizar_tarea/id
    path('actualizar_estado_tarea/<id>', actualizar_estado_tarea, name="actualizar_tarea"), # http://127.0.0.1:8000/api/actualizar_estado_tarea/id
    path('agregar_tarea/', agregar_tarea, name="agregar_tarea") # http://127.0.0.1:8000/api/agregar_tarea/
]