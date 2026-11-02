from django.db import models


class Teacher(models.Model):
    full_name = models.CharField(
        max_length=200,
        verbose_name="Мугалимдин аты-жөнү"
    )

    subject = models.CharField(
        max_length=150,
        verbose_name="Окуткан предмети же кызматы"
    )

    description = models.TextField(
        blank=True,
        verbose_name="Кыскача маалымат"
    )

    image = models.ImageField(
        upload_to='teachers/',
        blank=True,
        null=True,
        verbose_name="Сүрөтү"
    )

    is_published = models.BooleanField(
        default=True,
        verbose_name="Сайтта көрсөтүү"
    )

    class Meta:
        ordering = ['full_name']
        verbose_name = "Мугалим"
        verbose_name_plural = "Мугалимдер"

    def __str__(self):
        return self.full_name