from django.db import models


class Sermon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    preacher = models.CharField(max_length=100, verbose_name="Predicador")
    date = models.DateField(verbose_name="Fecha")
    audio_file = models.FileField(
        upload_to="sermons/audio/", verbose_name="Archivo de audio"
    )
    image = models.ImageField(
        upload_to="sermons/images/", blank=True, null=True, verbose_name="Imagen"
    )
    description = models.TextField(verbose_name="Descripción")
    bible_text = models.CharField(
        max_length=100, blank=True, verbose_name="Texto bíblico"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        verbose_name = "Sermón"
        verbose_name_plural = "Sermones"

    def __str__(self):
        return f"{self.title} - {self.date}"
