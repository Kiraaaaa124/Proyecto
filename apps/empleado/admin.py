from django.contrib import admin
from apps.empleado.models import Empleado, Habilidades
from datetime import date


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'email',
        'departamento',
        'edad', 
    )
    
    search_fields = ('nombre', 'apellido')
    
    list_filter = ('departamento', 'trabajo')
    
    def edad(self, obj):
        today = date.today()
        return today.year - obj.fecha_nac.year - ((today.month, today.day) < (obj.fecha_nac.month, obj.fecha_nac.day))
    edad.short_description = 'Edad'

admin.site.register(Habilidades)
admin.site.register(Empleado, EmpleadoAdmin)
