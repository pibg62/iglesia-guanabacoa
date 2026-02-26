from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "is_published")
    list_filter = ("author", "is_published", "published_date")
    search_fields = ("title", "content")
    date_hierarchy = "published_date"
    actions = ["make_published", "make_unpublished"]

    def make_published(self, request, queryset):
        queryset.update(is_published=True)

    make_published.short_description = "Publicar seleccionados"

    def make_unpublished(self, request, queryset):
        queryset.update(is_published=False)

    make_unpublished.short_description = "Ocultar seleccionados"
