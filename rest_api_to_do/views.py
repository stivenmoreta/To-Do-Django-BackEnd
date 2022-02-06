from urllib import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

#Modelo
from .models import Tarea
#Serializers
from .serializers import TareaSerializer,TareaSerializerEliminar,TareaSerializerCambiarEstado


@api_view(['GET'])
def lista_tarea(request):
    """
    Lista de todas las tareas que no esten eliminadas
    """
    if request.method == 'GET':
        tarea = Tarea.objects.filter(eliminarTarea=False).all()
        serializer = TareaSerializer(tarea, many=True)
        return Response(serializer.data)

@api_view(['PUT'])
def actualizar_estado_tarea(request,id):
    """
    Actualizar el estado de la tarea, si esta completa o no
    """
    try:
        tarea = Tarea.objects.get(idTarea=id)
    except Tarea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TareaSerializerCambiarEstado(tarea, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def actualizar_tarea(request,id):
    """
    Actualizar informacion de la tarea
    """
    try:
        tarea = Tarea.objects.get(idTarea=id)
    except Tarea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TareaSerializer(tarea, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def eliminar_tarea(request,id):
    """
    Elimina la tarea cambiando su estado de eliminarTarea
    """
    try:
        tarea = Tarea.objects.filter(idTarea=id).first()
    except Tarea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TareaSerializerEliminar(tarea, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def agregar_tarea(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TareaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   


