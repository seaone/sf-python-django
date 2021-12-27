import datetime

from django.db import models
from django.utils.safestring import mark_safe


class Category(models.TextChoices):
    ABSTRACT = 'Abstract'
    AERIAL = 'Aerial'
    ARCHITECTURAL = 'Architectural'
    BLACK_WHITE = 'Black And White'
    CONCEPTUAL = 'Conceptual'
    FASHION = 'Fashion'
    FOOD = 'Food'
    HDR = 'HDR'
    LANDSCAPE = 'Landscape'
    MOBILE = 'Mobile'
    MACRO = 'Macro'
    NATURE = 'Nature'
    NIGHT = 'Night'
    PORTRAIT = 'Portrait'
    SPORTS = 'Sports'
    STREET = 'Street'
    SUNRISE = 'Sunrise'
    SUNSET = 'Sunset'
    TILT_SHIFT = 'Tilt Shift'
    TRAVEL = 'Travel'
    UNDERWATER = 'Underwater'
    URBAN = 'Urban'
    UNCATEGORIZED = 'uncategorized'
    WEDDING = 'Wedding'
    WILDLIFE = 'Wildlife'


class Album(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256, blank=True, null=True)
    category = models.CharField(max_length=256, choices=Category.choices, default=Category.UNCATEGORIZED)

    def get_photos(self):
        photos = ''
        for photo in self.photo_set.all():
            photos = photos + f'<figure>' \
                              f'<img src="{photo.image.url}" style="width:274px; height:274px; object-fit:cover" />' \
                              f'<figcaption>{photo.pub_date.strftime("%d/%m/%y %H:%M:%S")} {photo.name}</figcaption>' \
                              f'</figure>'

        return mark_safe(photos)

    get_photos.short_description = 'Photos'

    def __str__(self):
        return self.name


class Photo(models.Model):
    albums = models.ManyToManyField(Album)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now)

    def image_preview(self, size='48'):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" style="width:48px; height:48px; object-fit:cover" />')
        else:
            return 'No Image Found'

    image_preview.short_description = 'Image'

    def get_albums(self):
        if self.albums:
            names = []

            for album in self.albums.all():
                names.append(album.name)

            return ', '.join(names)

    get_albums.short_description = 'Albums'

    def __str__(self):
        return f'{self.pub_date.date()} {self.pub_date.time()} {self.name}'
