from django.db import models

# Create your models here.
class Tarea (models.Model):
    idTarea = models.AutoField(primary_key=True, verbose_name="Id de la tarea")
    textoTarea = models.CharField(max_length=25, blank=False, null=False, verbose_name="Texto de la tarea")
    eliminarTarea = models.BooleanField(null=False, default=False, verbose_name="Tarea Eliminada o no");
    estadoTarea = models.BooleanField(null=False, default=False, verbose_name="Tarea completa o no") 
    fechaRegistro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion de la tarea")
    fechaTermino = models.DateTimeField(verbose_name="Fecha de termino de la tarea")
    ultimaModificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha del ultimo cambio")

    def __str__(self):
        return self.textoTarea
