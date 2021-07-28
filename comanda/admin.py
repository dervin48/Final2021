from django.contrib import admin
from .models import *


class DetalleComandaInline(admin.TabularInline):
	model = DetalleComanda
	extra = 0 
#	autocomplete_fields = ['platillo']

class ComandaAdmin(admin.ModelAdmin):
	inlines =[DetalleComandaInline]
	search_fields = ['fecha__fecha_comanda']
	list_filter = ['fecha_comanda','empleado']
	list_display = ['cliente','empleado','fecha_comanda','total']
	#readonly_field = ['total']

admin.site.register(Comanda, ComandaAdmin)
