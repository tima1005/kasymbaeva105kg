from django.contrib import admin
from django.utils.html import format_html
from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display = (
        'image_preview',
        'title',
        'created_at',
        'is_published',
    )

    list_filter = (
        'is_published',
        'created_at',
    )

    search_fields = (
        'title',
        'description',
    )

    readonly_fields = (
        'created_at',
        'image_preview',
    )

    list_editable = (
        'is_published',
    )

    list_per_page = 24

    @admin.display(description="Сүрөт")
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="75" height="55" '
                'style="object-fit:cover;border-radius:8px;" />',
                obj.image.url
            )
        return "Сүрөт жок"