from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Иш-чаранын аталышы")
    description = models.TextField(verbose_name="Маалымат")
    image = models.ImageField(
        upload_to='events/',
        blank=True,
        null=True,
        verbose_name="Сүрөт"
    )
    event_date = models.DateField(verbose_name="Өткөрүлүү күнү")
    location = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Өткөрүлүү жери"
    )
    is_published = models.BooleanField(default=True, verbose_name="Жарыялоо")

    class Meta:
        ordering = ['-event_date']
        verbose_name = "Иш-чара"
        verbose_name_plural = "Иш-чаралар"

    def __str__(self):
        return self.title