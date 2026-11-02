from django.db import models


class SchoolStatistic(models.Model):
    student_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Окуучулардын саны"
    )

    teacher_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Мугалимдердин саны"
    )

    class_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Класстардын саны"
    )

    founded_year = models.PositiveIntegerField(
        default=0,
        verbose_name="Түзүлгөн жылы"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Жаңыртылган убакыт"
    )

    class Meta:
        verbose_name = "Мектеп статистикасы"
        verbose_name_plural = "Мектеп статистикасы"

    def __str__(self):
        return "Мектеп статистикасы"


class EducationDetail(models.Model):
    title = models.CharField(max_length=200, verbose_name="Бөлүмдүн аталышы")
    slug = models.SlugField(unique=True, verbose_name="URL")
    short_description = models.TextField(verbose_name="Кыскача маалымат")
    content = models.TextField(verbose_name="Толук маалымат")
    image = models.ImageField(
        upload_to="education/",
        blank=True,
        null=True,
        verbose_name="Сүрөт"
    )
    is_published = models.BooleanField(default=True, verbose_name="Жарыялоо")
    order = models.PositiveIntegerField(default=0, verbose_name="Ирети")

    class Meta:
        ordering = ["order"]
        verbose_name = "Окуу багыты"
        verbose_name_plural = "Окуу багыттары"

    def __str__(self):
        return self.title





class ContactMessage(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Аты-жөнү"
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="Телефон"
    )

    email = models.EmailField(
        blank=True,
        verbose_name="Электрондук почта"
    )

    message = models.TextField(
        verbose_name="Билдирүү"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Жөнөтүлгөн убакыт"
    )

    is_read = models.BooleanField(
        default=False,
        verbose_name="Окулду"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Билдирүү"
        verbose_name_plural = "Келген билдирүүлөр"

    def __str__(self):
        return self.name