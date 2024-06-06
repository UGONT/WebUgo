from django.shortcuts import render
from .models import Mensaje

# Create your views here.

def index(request):
    """context: paquete variables que pueden ser consumidas por el front"""
    context = {}
    return render(request, "pages/index.html", context)

def comics(request):
    context = {}
    return render(request, "pages/comics.html", context)

def contacto(request):

    if request.method != "POST":

        context = {      
        }
        return render(request, "pages/contacto.html", context)
    
    else:

        nombre = request.POST["nombre"]
        email = request.POST["correo"]
        asunto = request.POST["asunto"]
        mensaje = request.POST["mensaje"]

        obj = Mensaje.objects.create(
            nombre = nombre,
            email = email,
            asunto = asunto,
            mensaje = mensaje,
        )
        obj.save
        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request, "pages/contacto.html", context)

def nosotros(request):
    context = {}
    return render(request, "pages/nosotros.html", context)

def sesion(request):
    context = {}
    return render(request, "pages/inicioSesion.html", context)

def registro(request):
    context = {}
    return render(request, "pages/registrarSesion.html", context)

def mensajes(request):
    mensajes = Mensaje.objects.all()
    context = {
        'mensajes': mensajes
    }
    return render(request, "pages/mensajes.html", context)