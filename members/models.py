from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    # Relación con usuario de Django (opcional)
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Usuario"
    )

    # Datos personales
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name1 = models.CharField(max_length=100, verbose_name="Primer apellido")
    last_name2 = models.CharField(
        max_length=100, blank=True, verbose_name="Segundo apellido"
    )
    birth_date = models.DateField(verbose_name="Fecha de nacimiento")
    baptism_date = models.DateField(
        verbose_name="Fecha de bautismo",
        blank=True,  # Permite vacío en formularios
        null=True,  # Permite NULL en base de datos
    )

    # Contacto
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    address = models.CharField(max_length=255, verbose_name="Dirección")
    reparto = models.CharField(max_length=100, verbose_name="Reparto")
    municipality = models.CharField(
        max_length=100, default="Guanabacoa", verbose_name="Municipio"
    )

    # Metadatos
    registered_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de registro"
    )
    ESTADO_CHOICES = [
        ("miembro", "Miembro"),
        ("congregado", "Congregado"),
    ]

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default="congregado",
        verbose_name="Estado",
    )
    photo = models.ImageField(
        upload_to="members/photos/", blank=True, null=True, verbose_name="Foto"
    )
    notes = models.TextField(blank=True, verbose_name="Notas adicionales")

    class Meta:
        verbose_name = "Miembro"
        verbose_name_plural = "Miembros"
        ordering = ["last_name1", "last_name2", "first_name"]

    def __str__(self):
        return f"{self.last_name1} {self.last_name2}, {self.first_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name1} {self.last_name2}".strip()
