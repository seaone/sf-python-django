from rest_framework import serializers

from albums.models import Album, Photo


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['category', 'description', 'id', 'name']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['description', 'id', 'image', 'name']
