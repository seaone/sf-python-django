from django.contrib import admin

from .models import Album, Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'pub_date', 'get_albums')


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ['get_photos']


admin.site.register(Album, AlbumAdmin)

admin.site.register(Photo, PhotoAdmin)
