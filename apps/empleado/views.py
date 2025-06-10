from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from apps.empleado.models import Empleado

class IndexView(TemplateView):
    template_name = 'empleados/home.html'

class ListaEmpleadoView(ListView):
    model = Empleado
    template_name = 'empleados/lista_empleados.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_empleados'] = context['object_list']
        return context
    
class CrearEmpleadoView(CreateView):
    model = Empleado
    fields = ['nombre','apellido','email','fecha_nac','pais','trabajo','departamento','habilidades']
    template_name = 'empleados/crear_empleado.html'
    success_url = reverse_lazy('lista_empleados')

class UpdateEmpleadoView(UpdateView):
    model = Empleado
    fields = ['nombre','apellido','email','fecha_nac','pais','trabajo','departamento','habilidades',]
    template_name = 'empleados/editar_empleado.html'
    success_url = reverse_lazy('lista_empleados')

class DeleteEmpleadoView(DeleteView):
    model = Empleado
    template_name = 'empleados/eliminar_empleado.html'
    success_url = reverse_lazy('lista_empleados')

class DetailEmpleadoView(DetailView):
    model = Empleado
    template_name = 'empleados/detalle_empleado.html'