from django.db import models


class Achievement(models.Model):
    title = models.CharField(max_length=200, verbose_name="Жетишкендиктин аталышы")
    description = models.TextField(verbose_name="Маалымат")
    image = models.ImageField(
        upload_to='achievements/',
        blank=True,
        null=True,
        verbose_name="Диплом же сүрөт"
    )
    year = models.PositiveIntegerField(verbose_name="Жылы")
    is_published = models.BooleanField(default=True, verbose_name="Жарыялоо")

    class Meta:
        ordering = ['-year']
        verbose_name = "Жетишкендик"
        verbose_name_plural = "Жетишкендиктер"

    def __str__(self):
        return self.title