from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=200, verbose_name="Сүрөттүн аталышы")
    image = models.ImageField(
        upload_to='gallery/',
        verbose_name="Сүрөт"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Сүрөт жөнүндө"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name="Жарыялоо")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"

    def __str__(self):
        return self.title