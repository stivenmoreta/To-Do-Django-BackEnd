# Generated by Django 3.2.9 on 2022-02-01 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_to_do', '0006_tarea_ultimamodificacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='tituloTarea',
        ),
        migrations.AlterField(
            model_name='tarea',
            name='textoTarea',
            field=models.CharField(max_length=20, verbose_name='Texto de la tarea'),
        ),
    ]