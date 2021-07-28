from django.contrib import admin
from .models import *



class MenuAdmin(admin.ModelAdmin):
	search_fields = ['descripcion']
	list_display = ['descripcion','precio']

admin.site.register(Menu,MenuAdmin)
# Register your models here.


