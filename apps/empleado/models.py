from django.db import models
from apps.departamento.models import Departamento
from datetime import date

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades de empleado'
        ordering = ['habilidad']
        unique_together = ('habilidad',)

    def __str__(self):
        return self.habilidad

class Empleado(models.Model):
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrativo'),
        ('2', 'Desarrollador'),
        ('3', 'Analista funcional'),
        ('4', 'Otro'),
    )

    nombre = models.CharField('Nombre', max_length=60)
    apellido = models.CharField('Apellido', max_length=60)
    email = models.EmailField(default="empleado@empresa.com")
    fecha_nac = models.DateField('Fecha de Nacimiento')
    pais = models.CharField(max_length=100, null=True, blank=True, default="No especificado")
    trabajo = models.CharField('Puesto', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)

    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-nombre', 'apellido']
        unique_together = ('nombre', 'departamento')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def calcularEdad(self):
        today = date.today()
        age = today.year - self.fecha_nac.year - ((today.month, today.day) < (self.fecha_nac.month, self.fecha_nac.day))
        return age
    calcularEdad.short_description = 'Edad'

