from django.contrib import admin
from . import models
# Register your models here.

class ArmasRegistradas(admin.ModelAdmin):
    list_display  = ['Nombre','Calibre','Descripcion']
    search_fields = ['Nombre','Calibre']
    list_filter   = ['Calibre']
    list_per_page = 10

class RegistroUser(admin.ModelAdmin):
    list_display=['Nombre_de_usuario','contraseña']
admin.site.register(models.Arma)
admin.site.register(models.TParma)