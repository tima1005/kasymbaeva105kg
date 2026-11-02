from django.contrib import admin
from .models import Achievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'year',
        'is_published',
    )

    list_filter = (
        'year',
        'is_published',
    )

    search_fields = (
        'title',
        'description',
    )

    list_editable = (
        'is_published',
    )

    list_per_page = 20