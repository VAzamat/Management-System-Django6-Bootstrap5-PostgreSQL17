from django.contrib import admin
from .models import Banner, GymActivity, PhotoAlbum, ImageGallery
from unfold.admin import ModelAdmin

#admin.site.register(Banner)
@admin.register(Banner)
class BannerAdmin(ModelAdmin):
    list_display = ('title', 'image_tag', 'link_url', 'is_active')
    list_filter = ('is_active',)
    readonly_fields = ('image_tag',)

@admin.register(GymActivity)
class GymActivityAdmin(ModelAdmin):
    list_display = ('title', 'image_tag', 'is_active')
    list_filter = ('is_active',)
    readonly_fields = ('image_tag',)


@admin.register(PhotoAlbum)
class PhotoAlbumAdmin(ModelAdmin):
    list_display = ('title', 'image_tag', 'is_active', 'formatted_created_at')
    list_filter = ('is_active',)
    readonly_fields = ('image_tag',)
    ordering = ('created_at',)


    #для форматирования даты
    @admin.display(description='Дата загрузки', ordering='created_at')
    def formatted_created_at(self, obj):
        return obj.created_at.strftime("%d.%m.%Y %H:%M")



@admin.register(ImageGallery)
class ImageGalleryAdmin(ModelAdmin):
    list_display = ('title', 'image_tag', 'is_active', 'album', 'formatted_created_at')
    list_filter = ('is_active',)
    ordering = ('album', 'order', 'created_at')

    #для форматирования даты
    @admin.display(description='Дата загрузки', ordering='created_at')
    def formatted_created_at(self, obj):
        return obj.created_at.strftime("%d.%m.%Y %H:%M")
