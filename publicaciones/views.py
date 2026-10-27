from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("Bienvenidos a Glups")

def lista_publicaciones(request):
    return HttpResponse("Estas son las publicaciones de Glups")