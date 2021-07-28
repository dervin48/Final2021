from django.db import models
from datetime import datetime

class Menu(models.Model):
	descripcion = models.CharField('descripcion',max_length=50)
	precio = models.DecimalField('precio', max_digits=8, decimal_places=2)


	def __str__(self):
		return "%s : %s" % (self.descripcion, self.precio)

	class Meta():
		db_table = 'menu'
		verbose_name='Menu'
		verbose_name_plural = 'Menus'


	
	