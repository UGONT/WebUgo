from django.db import models

# entrar al panel de django
# admin
# 1234


# Create your models here.
class Mensaje(models.Model):
    id_mensaje = models.AutoField(primary_key=True, db_column='idMensaje')
    nombre = models.CharField(max_length=14)
    email = models.EmailField(max_length=100, unique=False, blank=False, null=False)
    asunto = models.CharField(max_length=30, null=False)
    mensaje = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return (
            str(self.nombre)
            + ", Asunto: "
            + str(self.asunto)
            + ", Mensaje: "
            + str(self.mensaje)
        )
    
class Usuario(models.Model):
    email = models.EmailField(primary_key=True, max_length=100, unique=True, blank=False)
    nombre = models.CharField(max_length=14)
    password = models.CharField(max_length=16)
    
    def __str__(self):
        return (
            str(self.nombre)
            + ", Correo: "
            + str(self.email)
        )

class Comic(models.Model):
    id_comic = models.AutoField(primary_key=True, db_column='idComic')
    editorial = models.CharField(max_length=10, null=False, blank=False)
    titulo = models.CharField(max_length=70, null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    autor = models.CharField(max_length=200, null=False, blank=False)
    idioma = models.CharField(max_length=10, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    formato = models.CharField(max_length=50, null=False, blank=False)
    disponible = models.IntegerField(null=False, blank=False)
    edi_original = models.TextField(null=False, blank=False)
    isbn = models.CharField(max_length=20, null=True, blank=False, unique=True )
    ruta_img = models.CharField(max_length=35, null=True, blank=False)

    def __str__(self):
        return (
            str(self.titulo)
            + ", disponible: "
            + str(self.disponible)
        )

