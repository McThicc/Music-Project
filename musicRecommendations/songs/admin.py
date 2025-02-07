from django.contrib import admin

from .models import Artist, Song, Genre

#All the collections I have at the moment that need to be admin-ified
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Song)
