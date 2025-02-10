from django.contrib import admin

from .models import Artist, Song, Genre, Album

#All the collections I have at the moment that need to be admin-ified
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(Album)