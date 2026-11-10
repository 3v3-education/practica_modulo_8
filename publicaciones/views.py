from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactoForm
from .models import Publicacion


# Create your views here.
def base(request):
    return render (request, "publicaciones/base.html")

def inicio(request):
    return render(request, "publicaciones/inicio.html")

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.filter(estado="publicado").order_by("-fecha_creacion")
    contexto = {"publicaciones": publicaciones }
    return render(request, "publicaciones/lista_publicaciones.html", contexto)

def lista_autores(request):
    autores = [
        {"nombre":"Camila", "post": 3},
        {"nombre":"Evelyn", "post": 5},
        {"nombre":"Pedro", "post": 2}
        ]
    contexto = {"autores": autores}
    return render(request, "publicaciones/lista_autores.html", contexto)

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            correo = form.cleaned_data["correo"]
            asunto = form.cleaned_data["asunto"]
            mensaje = form.cleaned_data["mensaje"]

            print("Nombre:",nombre)
            print("Correo:",correo)
            print("Asunto:",asunto)
            print("Mensaje:",mensaje)
            return render(request, "publicaciones/contacto_exito.html", {"nombre":nombre})
    else:
        form = ContactoForm()
    return render (request, "publicaciones/contacto.html",{"form":form})