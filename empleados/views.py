from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
  TemplateView,
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView,
)

#importar el modelo Empleado
from .models import Empleado

#import forms
from .forms import EmpleadoForm

# Create your views here.
class InicioView(TemplateView):
  """ vista pagina de inicio"""
  template_name = 'inicio.html'


#1-Listar todos los empleados de la empresa
class ListaAllEmpleados(ListView):
  template_name = 'empleados/list_all.html'
  ordering = 'first_name'
  paginate_by = 6
  model = Empleado

  def get_queryset(self):
    palabra_clave = self.request.GET.get("kword", '')
    lista = Empleado.objects.filter(
      first_name__icontains=palabra_clave
    )
    return lista

#2-Listar todos los empleados que pertenecen a una area de la empresa
class ListByAreaEmpleado(ListView):
  template_name = 'empleados/list_by_area.html'
  context_object_name = 'empleados'

  def get_queryset(self):
    #el codigo que se necesita
    area = self.kwargs['shor_name']
    lista = Empleado.objects.filter(
      departamento__shor_name = area
    )
    return lista
  
class ListEmpleadosAdmin(ListView):
  template_name = 'empleados/lista_empleados.html'
  paginate_by = 5
  ordering = 'first_name'
  model = Empleado
  context_object_name = 'empleados'


#3-Listar los empleados por palabra clave (buscador: Juan)
class ListEmpleadoByKword(ListView):
  """Listar empleados por palabra clave"""
  template_name = 'empleados/by_kword.html'
  context_object_name = 'empleados'

  def get_queryset(self):
    print('''''''''''')
    palabra_clave = self.request.GET.get("kword", '')
    lista = Empleado.objects.filter(
      first_name= palabra_clave
    )
    return lista


#4-Listar habilidades de un empleado
class ListaHabilidadesEmpleado(ListView):
  template_name = 'empleados/habilidades.html'
  context_object_name = 'habilidades'

  def get_queryset(self):
    empleado = Empleado.objects.get(id=8)
    return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
  template_name = 'empleados/detail_empleados.html'
  model = Empleado

  def get_context_data(self, **kwargs):
    context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
    context['titulo'] = 'Empleado del mes'
    return context 

#create success
class SuccessView(TemplateView):
  template_name = 'empleados/success.html'

#permite crear un empleado
class EmpleadoCreateView(CreateView):
  template_name = 'empleados/add.html'
  model = Empleado
  form_class = EmpleadoForm
  success_url = reverse_lazy('empleado_app:empleados_admin')

  def form_valid(self, form):
      empleado = form.save(commit=False)
      empleado.save()
      return super(EmpleadoCreateView, self).form_valid(form)
  
#permite actualizar el empleado
class EmpleadoUpdateView(UpdateView):
  template_name = "empleados/update.html"
  model = Empleado
  fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
  success_url = reverse_lazy('empleado_app:empleados_admin')


  def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    print("Metodo Post")
    print(request.POST)
    return super().post(request, *args, **kwargs)
  
  def form_valid(self, form):
    form
    return super(EmpleadoUpdateView, self).form_valid(form)
  
#permite eliminar empleado
class EmpleadoDeleteView(DeleteView):
  template_name = "empleados/delete.html"
  model = Empleado
  success_url = reverse_lazy('empleado_app:empleados_admin')