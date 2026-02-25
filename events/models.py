from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    date = models.DateTimeField(verbose_name="Fecha y hora")
    location = models.CharField(max_length=200, verbose_name="Lugar")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(
        upload_to="events/", blank=True, null=True, verbose_name="Imagen"
    )
    is_featured = models.BooleanField(default=False, verbose_name="Destacado")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date"]
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.title
