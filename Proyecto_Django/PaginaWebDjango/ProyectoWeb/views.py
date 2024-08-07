from django.shortcuts import render, redirect
from .models import Mensaje,Comic, Usuario
import pandas as pd
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

# Create your views here.
# pip install pandas, openpyxl
def index(request):
    comics = Comic.objects.all()
    context = {
        'comics': comics,
    }
    if request.user.is_authenticated:
        context['user'] = request.user
    else:
        context['user'] = None
    return render(request, "pages/index.html", context)

def comics(request):
    comics = Comic.objects.all()
    context = {
        'comics' : comics
    }
    if request.user.is_authenticated:
        context['user'] = request.user
    else:
        context['user'] = None
    return render(request, "pages/comics.html", context)

def contacto(request):

    if request.method != "POST":
        context = {      
        }
        if request.user.is_authenticated:
            context['user'] = request.user
        else:
            context['user'] = None
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
    if request.user.is_authenticated:
        context['user'] = request.user
    else:
        context['user'] = None
    return render(request, "pages/nosotros.html", context)

def registro(request):

    if request.method != "POST":
        context = {} 
        return render(request, "pages/registrarSesion.html", context)  
    else:
        email = request.POST.get("txtEmail")
        usuario = request.POST.get("txtUser")
        password = request.POST.get("txtPass")

        obj = Usuario.objects.create(

            email = email,
            nombre = usuario,
            password = password
        )
        obj.save()
        
        context = {
            'mensaje' : "Registro exitoso"
        }
        return render(request, "pages/inicioSesion.html", context)

    

def mensajes(request):
    mensajes = Mensaje.objects.all()
    context = {
        'mensajes': mensajes
    }
    return render(request, "pages/admin/mensajes.html", context)

def mensaje_del(request, pk):
    try:
        mensaje = Mensaje.objects.get(id_mensaje = pk)
        mensaje.delete()
        mensajes = Mensaje.objects.all()
        context = {
            'mensaje' : "Eliminado con exito",
            'mensajes': mensajes, 
        }
        return render(request, "pages/admin/mensajes.html", context)

    except:
        mensajes = Mensaje.objects.all()
        context = {
            'mensaje' : "Error al eliminar el mensaje",
            'mensajes': mensajes, 
        }
        
        return render(request, "pages/admin/mensajes.html", context)

@login_required
def subirComics(request):

    if request.user.is_superuser or request.user.groups.filter(name='administrador').exists():
        if request.method != "POST":
            context = {      
            }
            return render(request, "pages/admin/subirComics.html", context)
        
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
            return render(request, "pages/admin/subirComics.html", context)

        else:
            try:
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
                obj.save()
                context = {
                    "mensaje": "Registro Exitoso",
                }
                context = {}
                return render(request, "pages/admin/subirComics.html", context)
            except Exception as e:
                context = {
                "mensaje": "Ocurrió un error al registrar el comic",
                "error": str(e),
                }
                return render(request, "pages/admin/subirComics.html", context)
    else:
        return redirect("index")
    

def verComic(request, pk):

    comic = Comic.objects.get(id_comic = pk)

    context = {
        'comic' : comic,
    }
    return render(request, "pages/vistaComic.html", context)

def comic_del(request, pk):
    try:
        comic = Comic.objects.get(id_comic = pk)
        comic.delete()
        comics = Comic.objects.all()
        context = {
            'mensaje' : "Eliminado con exito",
            'comics': comics, 
        }
        return render(request, "pages/admin/crud_comics.html", context)

    except:
        comics = Comic.objects.all()
        context = {
            'mensaje' : "Error al eliminar el comic",
            'comics': comics, 
        }
        
        return render(request, "pages/admin/crud_comics.html", context)



  
def comic_find(request, pk):
    comic = Comic.objects.get(id_comic = pk)
    context = {
        'comic':comic,
    }
    return render(request, "pages/admin/editComic.html", context)

def comic_edit(request,pk):
    comic = Comic.objects.get(id_comic = pk)
    if request.method=="POST":

        comic.editorial = request.POST.get('editorial')
        comic.titulo = request.POST.get('titulo')
        comic.precio = request.POST.get('precio')
        comic.autor = request.POST.get('autores')
        comic.idioma = request.POST.get('idioma')
        comic.descripcion = request.POST.get('descripcion')
        comic.formato = request.POST.get('formato')
        comic.disponible = request.POST.get('disponibles')
        comic.edi_original = request.POST.get('editorial_original')
        comic.isbn = request.POST.get('isbn')
        comic.ruta_img= request.POST.get('ruta_imagen')

        comic.save()
        comics = Comic.objects.all()
        context = {
            "mensaje": "Modificado con Exito",
            'comics' : comics
        }
        return render(request, "pages/admin/crud_comics.html", context)
    
@login_required
def crudComics(request):
    if request.user.is_superuser or request.user.groups.filter(name='administrador').exists():
        comics = Comic.objects.all()
        context = {
            'comics': comics
        }
        return render(request, "pages/admin/crud_comics.html", context)
    else:
        return redirect('index')


def sesion(request):
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser or user.groups.filter(name='administrador').exists():
                comics = Comic.objects.all()
                context = {
                    "comics": comics,
                }
                return render(request, "pages/admin/crud_comics.html", context)
            else:
                return redirect('index')  
        else:
            context = {
                "mensaje": "Usuario o contraseña incorrecta",
                "design": "alert alert-danger w-50 mx-auto text-center",
            }
            return render(request, "pages/inicioSesion.html", context)
    else:
        context = {}
        if request.user.is_authenticated:
            context['user'] = request.user
        else:
            context['user'] = None
        return render(request, "pages/inicioSesion.html", context)
    

def desconectar(request):   
    if request.user.is_authenticated:
        logout(request)
    context = {
        "mensaje":"Desconectado con exito",
        "user" : None
    }
    
    return render(request,"pages/inicioSesion.html",context)

def perfil(request):
    context = {}
    return render(request,"pages/perfil.html", context)