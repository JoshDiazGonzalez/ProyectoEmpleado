from django.db import models

# Create your models here.
class Departamento(models.Model):
  name = models.CharField('Nombre', max_length=50)
  shor_name = models.CharField('Nombre Corto', max_length=20, unique=True)
  anulate = models.BooleanField('Anulado', default=False)

  class Meta:
    verbose_name = "Mi Departamento"
    verbose_name_plural = "Areas de la Empresa"
    ordering = ['-name']

  def __str__(self):
    return str(self.id) + '-' + self.name + '-' + self.shor_name