from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ["idTarea","textoTarea","estadoTarea","fechaTermino"]

class TareaSerializerCambiarEstado(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ["idTarea","estadoTarea"]

class TareaSerializerEliminar(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ["idTarea","eliminarTarea"]