from django.db import models
import uuid

from django.utils.safestring import mark_safe

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
    link_url = models.CharField(
        max_length=50,
        verbose_name="Выбираемая ссылка"
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

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="100" style="object-fit:cover; border-radius:5px;"/>')
        return "Нет изображения"

    image_tag.short_description = 'Предпросмотр'

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
    link_url = models.CharField(
        max_length=50,
        verbose_name="Якорь - Ссылка перенаправления"
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

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="100" style="object-fit:cover; border-radius:5px;"/>')
        return "Нет изображения"

    image_tag.short_description = 'Предпросмотр'

