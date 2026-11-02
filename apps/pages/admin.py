from django.contrib import admin
from .models import SchoolStatistic, EducationDetail, ContactMessage


@admin.register(SchoolStatistic)
class SchoolStatisticAdmin(admin.ModelAdmin):
    list_display = (
        "student_count",
        "teacher_count",
        "class_count",
        "founded_year",
        "updated_at",
    )


@admin.register(EducationDetail)
class EducationDetailAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_published", "order")
    list_editable = ("is_published", "order")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "phone", "email", "message")
    list_editable = ("is_read",)
    readonly_fields = ("created_at",)