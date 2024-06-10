from django.shortcuts import render
from .models import Mensaje,Comic
import pandas as pd

# Create your views here.

def index(request):
    comics = Comic.objects.all()
    context = {
        'comics' : comics
    }
    return render(request, "pages/index.html", context)

def comics(request):
    comics = Comic.objects.all()
    context = {
        'comics' : comics
    }
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
    
def subirComics(request):

    if request.method != "POST":
        context = {      
        }
        return render(request, "pages/subirComics.html", context)
    
    elif 'file' in request.FILES:
        excel_file = request.FILES['file']
        df = pd.read_excel(excel_file, engine='openpyxl')

        for index, row in df.iterrows():
                obj = Comic.objects.create(
                    editorial=row['Editorial'],
                    titulo=row['Titulo'],
                    precio=row['Precio'],
                    autor=row['Autor(es)'],
                    idioma=row['Idioma'],
                    descripcion=row['Descripción'],
                    formato=row['Formato'],
                    disponible=row['Cantidad'],
                    edi_original=row['Edición original'],
                    isbn=row['ISBN'],
                    ruta_img=row['Ruta']
                    )
                obj.save()
        context = {
            'mensaje': "Registro exitoso",
        }
        return render(request, "pages/subirComics.html", context)

    else:

        editorial = request.POST.get('editorial')
        titulo = request.POST.get('titulo')
        precio = request.POST.get('precio')
        autores = request.POST.get('autores')
        idioma = request.POST.get('idioma')
        descripcion = request.POST.get('descripcion')
        formato = request.POST.get('formato')
        disponibles = request.POST.get('disponibles')
        editorial_original = request.POST.get('editorial_original')
        isbn = request.POST.get('isbn')
        ruta_imagen = request.POST.get('ruta_imagen')

        obj = Comic.objects.create(

            editorial = editorial,
            titulo = titulo,
            precio = precio,
            autor = autores,
            idioma = idioma,
            descripcion = descripcion,
            formato = formato,
            disponible = disponibles,
            edi_original = editorial_original,
            isbn = isbn,
            ruta_img = ruta_imagen,

        )
        obj.save
        context = {
            "mensaje": "Registro Exitoso",
        }
        context = {}
        return render(request, "pages/subirComics.html", context)
    

def verComic(request, pk):

    comic = Comic.objects.get(id_comic = pk)

    context = {
        'comic' : comic,
    }
    return render(request, "pages/vistaComic.html", context)