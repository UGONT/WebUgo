from django.shortcuts import render
from .models import Mensaje,Comic

# Create your views here.

def index(request):
    comics = Comic.objects.all()
    context = {
        'comics' : comics
    }
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

def mensaje_del(request, pk):
    try:
        mensaje = Mensaje.objects.get(id_mensaje = pk)
        mensaje.delete()
        mensajes = Mensaje.objects.all()
        context = {
            'mensaje' : "Eliminado con exito",
            'mensajes': mensajes, 
        }
        return render(request, "pages/mensajes.html", context)

    except:
        mensajes = Mensaje.objects.all()
        context = {
            'mensaje' : "Error al eliminar el mensaje",
            'mensajes': mensajes, 
        }
        
        return render(request, "pages/mensajes.html", context)