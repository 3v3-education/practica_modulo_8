from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "publicaciones/inicio.html")

def lista_publicaciones(request):
    publicaciones = [
        {"titulo": "Mi primer publicación", "autor":"Jorge"},
        {"titulo": "Aprendiendo Django", "autor":"Marcos"},
        {"titulo": "Vistas y Rutas", "autor":"Lucia"}
    ]
    contexto = {"publicaciones": publicaciones }
    return render(request, "publicaciones/lista_publicaciones.html", contexto)