from django.db import models
import uuid

from django.utils.safestring import mark_safe
from django.core.validators import MinValueValidator

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


class PhotoAlbum(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="Уникальный ID"
    )

    title = models.CharField(
        max_length=255,
        verbose_name="Название альбома"
    )

    cover_image = models.ImageField(
        upload_to='images/PhotoAlbumCovers/',
        verbose_name="Обложка альбома",
        **Nullable
    )

    description = models.TextField(
        verbose_name="Описание события",
        **Nullable
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Отображать на сайте"
    )

    class Meta:
        verbose_name = "Фотоальбом"
        verbose_name_plural = "Фотоальбомы"
        ordering = ['-created_at']

    def __str__(self):
        return f"Альбом - {self.title}"

    def image_tag(self):
        if self.cover_image:
            return mark_safe(f'<img src="{self.cover_image.url}" height="100" style="object-fit:cover; border-radius:5px;"/>')
        return "Нет изображения"

    image_tag.short_description = 'Предпросмотр'


class ImageGallery(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID для фото"
    )
    album = models.ForeignKey(
        PhotoAlbum,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name="Альбом"
    )
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок фото"
    )
    image = models.ImageField(
        upload_to='images/ImageGallery/',
        verbose_name="Фотография"
    )
    category = models.CharField(
        max_length=100,
        verbose_name="Категория/Тег",
        **Nullable
    )
    description = models.TextField(
        verbose_name="Описание",
        **Nullable
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Порядок вывода"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата загрузки"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Отображать в галерее"
    )

    class Meta:
        verbose_name = "Фото галереи"
        verbose_name_plural = "Галерея изображений"
        ordering = ['order', '-created_at']  # Сначала по порядку, потом по новизне

    def __str__(self):
        return f"Фото - {self.title}"

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="100" style="object-fit:cover; border-radius:5px;"/>')
        return "Нет изображения"

    image_tag.short_description = 'Предпросмотр'

class SubscriptionPlanFeature(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название услуги")

    class Meta:
        verbose_name = "Услуга тарифного плана"
        verbose_name_plural = "Услуги тарифного плана"

    def __str__(self):
        return self.name


class SubscriptionPlan(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название тарифа"
    )
    features = models.ManyToManyField(
        SubscriptionPlanFeature,
        related_name="plans",
        verbose_name="Включенные услуги",
        blank=True
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание тарифа"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Стоимость (руб.)"
    )
    duration_days = models.PositiveIntegerField(
        default=30,
        verbose_name="Длительность (в днях)"
    )

    is_highlighted = models.BooleanField(
        default=True,
        verbose_name="Подсвеченный тариф"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Доступен для покупки"
    )

    class Meta:
        verbose_name = "Тарифный план"
        verbose_name_plural = "Тарифные планы"
        ordering = ['price']

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

