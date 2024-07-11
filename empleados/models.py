from django.db import models
#importar ckeditor
from ckeditor.fields import RichTextField # type: ignore
from departamentos.models import Departamento

# Create your models here.
class Habilidad(models.Model):
  habilidad = models.CharField('Habilidad', max_length=50)

  class Meta:
    verbose_name = "Habilidad"
    verbose_name_plural = "Habilidades Empleados"

  def __str__(self):
    return str(self.id) + '-' + self.habilidad



class Empleado(models.Model):
  """Modelo para la tabla empleado"""

  #CONTADOR
  #ADMINISTRADOR
  #ECONOMISTA
  #OTRO
  JOB_CHOICES = (
    ('0', 'CONTADOR'),
    ('1', 'ADMINISTRADOR'),
    ('2', 'ECONOMISTA'),
    ('3', 'OTRO'),
  )
  #atributos
  first_name = models.CharField('Nombre', max_length=50)
  last_name = models.CharField('Apellidos', max_length=20)
  job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
  image = models.ImageField(upload_to='empleado', blank=True, null=True)
  #creacion ForenKey
  departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
  habilidades = models.ManyToManyField(Habilidad)
  hoja_vida = RichTextField()

  def __str__(self):
    return str(self.id) + '-' + self.first_name + '-' + self.last_name
