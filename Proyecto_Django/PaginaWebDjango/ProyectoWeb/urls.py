from django.urls import path
from . import views

""" path('nombreURL',funcionVista,nombreDePagina) """
urlpatterns = [
    path('', views.index, name='index'),
    path('comics', views.comics, name='comics'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.nosotros, name='nosotros')
]