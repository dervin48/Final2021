from django.contrib import admin
from .models import *

class TelefonoInline(admin.TabularInline):
	model = Telefono
	extra = 0 
	autocomplete_fields = ['tipo']
	#raw_id_fields = ['tipo']


# Register your models here.
class EmpleadoAdmin(admin.ModelAdmin):
	inlines = [TelefonoInline] #Detalle dentro del modelo
	search_fields = ['nombre','apellido']
	list_filter = ['fecha_nacimiento']
	list_display = ['dpi','nombre','apellido','fecha_nacimiento','edad','correo']


admin.site.register(Empleado,EmpleadoAdmin)
