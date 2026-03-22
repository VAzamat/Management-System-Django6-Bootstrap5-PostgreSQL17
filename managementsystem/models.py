from django.db import models
import uuid

Nullable = {"null": True, "blank": True}

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
        verbose_name="Слоган баннера",
        **Nullable
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


class GymActivity(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="Уникальный ID"
    )
    title = models.CharField(
        max_length=60,
        verbose_name="Название",
    )
    slogan = models.TextField(
        verbose_name="Слоган баннера",
        **Nullable
    )
    subtitle = models.CharField(
        max_length=60,
        verbose_name="Название подсекции",
    )
    description = models.TextField(
        max_length=250,
        verbose_name="Описание",
        **Nullable
    )
    image = models.ImageField(
        upload_to='GymActivities/',
        verbose_name="Изображение",
        **Nullable
    )
    link_url = models.URLField(
        max_length=500,
        verbose_name="Ссылка на страницу",
        **Nullable
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Видимость"
    )

    class Meta:
        verbose_name = "Активность в зале"
        verbose_name_plural = "Активности в зале"

    def __str__(self):
        return self.title

