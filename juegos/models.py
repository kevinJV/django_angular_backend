from django.db import models

# Create your models here.

class Juegos(models.Model):
    # ID del row
    id = models.AutoField(primary_key=True)
    # Nombre del juego
    nombre = models.CharField(max_length=255, null=False)
    # Descripcion del juego
    descripcion = models.TextField()
    # Desarrolladora del juego
    empresa = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)