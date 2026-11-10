from django.contrib import admin
from .models import Publicacion

admin.site.site_header = "Administración de Glups"
admin.site.site_title = "Panel de Glups"
admin.site.index_title = "Gestión de contenidos"


# Register your models here.
class PostAdmin(admin.ModelAdmin):    
    list_display = ("titulo", "autor", "fecha_creacion", "estado")    
    search_fields = ("titulo", "contenido", "autor")    
    list_filter = ("estado", "fecha_creacion")
    list_editable = ("estado",)

admin.site.register(Publicacion, PostAdmin)