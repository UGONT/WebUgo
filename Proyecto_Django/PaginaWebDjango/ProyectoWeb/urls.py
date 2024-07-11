from django.urls import path
from . import views


""" path('nombreURL',funcionVista,nombreDePagina) """
urlpatterns = [
    path('', views.index, name='index'),
    path('comics', views.comics, name='comics'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('sesion/', views.sesion, name='sesion'),
    path('registro', views.registro, name='registro'),
    path('perfil', views.perfil, name='perfil'),
    path('mensajes', views.mensajes, name='mensajes'),
    path('mensaje_del/<str:pk>', views.mensaje_del, name='mensaje_del'),
    path('comic_del/<str:pk>', views.comic_del, name='comic_del'),
    path('subirComics', views.subirComics, name='subirComics'),
    path('verComic/<str:pk>', views.verComic, name='verComic'),
    path('comic_find/<str:pk>', views.comic_find, name='comic_find'),
    path('comic_edit/<str:pk>', views.comic_edit, name='comic_edit'),
    path('crudComics', views.crudComics, name='crudComics'),

    path("login", views.sesion, name="login"),
    path("logout", views.desconectar, name="logout"),
]