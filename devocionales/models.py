from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    published_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de publicación"
    )
    updated_date = models.DateTimeField(
        auto_now=True, verbose_name="Última actualización"
    )
    image = models.ImageField(
        upload_to="devocionales/", blank=True, null=True, verbose_name="Imagen"
    )
    is_published = models.BooleanField(default=True, verbose_name="Publicado")

    class Meta:
        ordering = ["-published_date"]
        verbose_name = "Devocional"
        verbose_name_plural = "Devocionales"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("devocionales:detail", args=[str(self.id)])
