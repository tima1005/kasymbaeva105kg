from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = (
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

    date_hierarchy = 'created_at'

    list_editable = (
        'is_published',
    )

    readonly_fields = (
        'created_at',
    )

    list_per_page = 20