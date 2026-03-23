from django.contrib import admin
from .models import Banner, GymActivity, PhotoAlbum, ImageGallery


#admin.site.register(Banner)
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'link_url', 'is_active')
    list_filter = ('is_active',)
    readonly_fields = ('image_tag',)

@admin.register(GymActivity)
class GymActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'is_active')
    list_filter = ('is_active',)
    readonly_fields = ('image_tag',)


@admin.register(PhotoAlbum)
class PhotoAlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'is_active')
    list_filter = ('is_active',)
    readonly_fields = ('image_tag',)

@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'is_active', 'album')
    list_filter = ('is_active',)
