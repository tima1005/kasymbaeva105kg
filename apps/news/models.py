from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Жаңылыктын аталышы")
    description = models.TextField(verbose_name="Толук маалымат")
    image = models.ImageField(
        upload_to='news/',
        blank=True,
        null=True,
        verbose_name="Сүрөт"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name="Жарыялоо")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Жаңылык"
        verbose_name_plural = "Жаңылыктар"

    def __str__(self):
        return self.title