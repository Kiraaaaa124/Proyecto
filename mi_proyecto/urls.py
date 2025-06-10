from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from apps.departamento.views import ListaDepartamentosView, CrearDepartamentosView, UpdateDepartamentoView, DeleteDepartamentoView, DetailDepartamentoView
from apps.empleado.views import ListaEmpleadoView, CrearEmpleadoView, UpdateEmpleadoView, DeleteEmpleadoView, DetailEmpleadoView, IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/', permanent=False)),
    path('home/', IndexView.as_view(), name='home'),
    #Urls Departamento
    path('departamentos/',ListaDepartamentosView.as_view(), name='lista_departamentos'),
    path('departamentos/crear/', CrearDepartamentosView.as_view(), name='crear_departamento'),
    path('departamentos/editar/<int:pk>/', UpdateDepartamentoView.as_view(), name='editar_departamento'),
    path('departamentos/eliminar/<int:pk>/', DeleteDepartamentoView.as_view(), name='eliminar_departamento'),
    path('departamentos/detalle/<int:pk>/', DetailDepartamentoView.as_view(), name='detalle_departamento'),
    #Urls empleado
    path('empleados/',ListaEmpleadoView.as_view(), name='lista_empleados'),
    path('empleados/crear/', CrearEmpleadoView.as_view(), name='crear_empleado'),
    path('empleados/editar/<int:pk>/', UpdateEmpleadoView.as_view(), name='editar_empleado'),
    path('empleados/eliminar/<int:pk>/', DeleteEmpleadoView.as_view(), name='eliminar_empleado'),
    path('empleados/detalle/<int:pk>/', DetailEmpleadoView.as_view(), name='detalle_empleado'),
]