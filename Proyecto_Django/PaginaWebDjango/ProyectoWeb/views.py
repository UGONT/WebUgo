from django.shortcuts import render

# Create your views here.

def index(request):
    """context: paquete variables que pueden ser consumidas por el front"""
    context = {}
    return render(request, "pages/index.html", context)

def comics(request):
    context = {}
    return render(request, "pages/comics.html", context)

def contacto(request):
    context = {}
    return render(request, "pages/contacto.html", context)

def nosotros(request):
    context = {}
    return render(request, "pages/nosotros.html", context)