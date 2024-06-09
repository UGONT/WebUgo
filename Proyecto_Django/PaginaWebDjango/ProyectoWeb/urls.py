from django.urls import path
from . import views


""" path('nombreURL',funcionVista,nombreDePagina) """
urlpatterns = [
    path('', views.index, name='index'),
    path('comics', views.comics, name='comics'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('sesion', views.sesion, name='sesion'),
    path('registro', views.registro, name='registro'),
    path('mensajes', views.mensajes, name='mensajes'),
    path('mensaje_del/<str:pk>', views.mensaje_del, name='mensaje_del'),
    path('subirComics', views.subirComics, name='subirComics'),
    path('verComic/<str:pk>', views.verComic, name='verComic'),
]