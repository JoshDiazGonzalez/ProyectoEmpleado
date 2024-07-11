from django.db import models

# Create your models here.
class Prueba(models.Model):
  #crear los atributos
  titulo = models.CharField(max_length=30)
  subtitulo = models.CharField(max_length=50)
  cantidad = models.IntegerField()

  def __str__(self) -> str:
    return self.titulo + '-' + self.subtitulo