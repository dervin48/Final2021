#- * -coding: utf-8 - * -
from django.db import models
from comun.models import Persona
from menu.models import Menu
from cliente.models import Cliente
from empleado.models import  Empleado
from .models import *

# Create your models here.

class Comanda(models.Model):
    cliente = models.ForeignKey(
          Cliente, verbose_name='Cliente', on_delete=models.CASCADE)
    empleado = models.ForeignKey(
          Empleado, verbose_name='Empleado', on_delete=models.CASCADE)
    fecha_comanda = models.DateField('fecha comanda',editable=False, auto_now_add=True)
    total = models.DecimalField('total', max_digits=10, 
          decimal_places=2,editable=False,default=0.00)

    def __str__(self):
        return "%s : %s" % (self.fecha_comanda, self.cliente)

    def save (self, **kwargs):
        monto=0
        for d in self.detallecomanda_set.all():
            monto += d.sub_total
        self.total = monto
        super(Comanda, self).save()

    class Meta():
        db_table = 'comanda'
        verbose_name='Comanda'
        verbose_name_plural = 'comandas'

class       DetalleComanda(models.Model):
    comanda = models.ForeignKey(
          Comanda, verbose_name='comanda', on_delete=models.CASCADE)
    menu = models.ForeignKey(
          Menu, verbose_name='Menu', on_delete=models.CASCADE)
    cantidad = models.IntegerField('cantidad')
    sub_total = models.DecimalField('sub_total', max_digits=10,
     decimal_places=2, default=0.00)
            
    def __str__(self):
            return "%s" % (self.comanda)
    
    def save(self, **kwargs):
        self.sub_total = self.menu.precio * self.cantidad
        
        super(DetalleComanda, self).save()

        self.total = self.sub_total
        super(Comanda,self).all(*args, **kwargs)


class Meta:
      db_table = 'comandadetalle'
      verbose_name='detalle de comanda'
      verbose_name_plural ='detalles de comanda'


