from django.contrib import admin
from .models import Publicacion

# Register your models here.
class PostAdmin(admin.ModelAdmin):    
    list_display = ("titulo", "autor", "fecha_creacion", "estado")    
    search_fields = ("titulo", "contenido", "autor")    
    list_filter = ("estado", "fecha_creacion")

admin.site.register(Publicacion, PostAdmin)