from django.contrib import admin
from django.utils.html import format_html
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    list_display = (
        'image_preview',
        'full_name',
        'subject',
        'is_published',
    )

    list_filter = (
        'is_published',
        'subject',
    )

    search_fields = (
        'full_name',
        'subject',
    )

    list_editable = (
        'is_published',
    )

    readonly_fields = (
        'image_preview',
    )

    list_per_page = 20

    @admin.display(description="Сүрөт")
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="65" height="65" '
                'style="object-fit:cover;border-radius:10px;" />',
                obj.image.url
            )
        return "Сүрөт жок"