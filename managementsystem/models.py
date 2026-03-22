from django.db import models
import uuid

class Banner(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="Уникальный ID"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название баннера"
    )
    slogan = models.TextField(
        blank=True,
        null=True,
        verbose_name="Слоган баннера"
    )
    button_text = models.CharField(
        max_length=100,
        verbose_name="Текст кнопки"
    )
    link_url = models.URLField(
        max_length=500,
        verbose_name="Ссылка перенаправления"
    )
    image = models.ImageField(
        upload_to='images/banners/',
        verbose_name="Изображение баннера"
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="Видимость баннера"
    )

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

    def __str__(self):
        return self.title

