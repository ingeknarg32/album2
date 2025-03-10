from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="eventos/", blank=True, null=True)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)  # Opcional, si el evento es presencial
    url_evento = models.URLField(blank=True, null=True)  # Enlace a inscripción o más info

    def __str__(self):
        return self.titulo
