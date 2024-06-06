from django.db import models

# Create your models here.
class Mensaje(models.Model):
    id_mensaje = models.AutoField(primary_key=True, db_column='idMensaje')
    nombre = models.CharField(max_length=14)
    email = models.EmailField(max_length=100, unique=False, blank=False, null=False)
    asunto = models.CharField(max_length=30)
    mensaje = models.CharField(max_length=200)
    def __str__(self):
        return (
            str(self.nombre)
            + ", Asunto: "
            + str(self.asunto)
            + ", Mensaje: "
            + str(self.mensaje)
        )