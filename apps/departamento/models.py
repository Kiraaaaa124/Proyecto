from django.db import models

class Departamento (models.Model):
    nombre=models.CharField('Departamento',max_length=50,blank=True)
    sigla=models.CharField('Sigla',max_length=4, unique=True)
    activo=models.BooleanField('¿Està activo?', default=False)
    piso=models.CharField('Piso',max_length=5,blank=True)
    oficina=models.CharField('Oficina Nº', max_length=10, blank=True)

    class Meta:
        verbose_name= 'Departamento'
        verbose_name_plural = 'Áreas de la empresa'
        ordering = ['nombre']
        unique_together = ('nombre', 'sigla')

    def __str__(self):
        return self.nombre
