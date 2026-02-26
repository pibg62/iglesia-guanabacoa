from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("full_name", "municipality", "phone")  # sin is_active
    list_filter = ("municipality", "reparto")  # sin is_active
    search_fields = ("first_name", "last_name1", "last_name2", "phone")
    date_hierarchy = "registered_date"

    fieldsets = (
        (
            "Datos personales",
            {
                "fields": (
                    "first_name",
                    "last_name1",
                    "last_name2",
                    "birth_date",
                    "baptism_date",
                    "estado",
                    "photo",
                )
            },
        ),
        ("Contacto", {"fields": ("phone", "address", "reparto", "municipality")}),
        ("Estado", {"fields": ("notes", "user")}),  # is_active eliminado
    )
