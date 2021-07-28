 #- * -coding: utf-8 - * -
from django.db import models
from comun.models import Persona, TipoTelefono

# Create your models here.

class Empleado (Persona):
	sueldo = models.CharField('sueldo',max_length=14,null=True, blank=True)
	dpi = models.CharField('dpi', max_length=14,unique=True,null=True, blank=True)

	class Meta():
		db_table = 'empleado'
		verbose_name='Empleado'
		verbose_name_plural = 'Empleados'

class Telefono(models.Model):
	empleado = models.ForeignKey(
		Empleado, verbose_name='Empleado', on_delete=models.CASCADE)
	numero = models.PositiveIntegerField(
		'numero de Telefono', help_text='solo incluir numeros'
    )
	tipo = models.ForeignKey(
		TipoTelefono,verbose_name='Tipo Telefono',related_name='TelEmpleado',on_delete=models.CASCADE)
    
	def __str__(self):
		return "%s : %s" % (self.empleado, self.numero)

	class Meta:
		verbose_name='Telefono de Empleado'
		verbose_name_plural = 'Telefonos de Empleado'