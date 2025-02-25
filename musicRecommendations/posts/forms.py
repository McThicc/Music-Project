from django import forms
from django.utils import timezone
from songs.models import Song, Genre, Album, Artist

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'featured_artists', 'album', 'genre']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre_name']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'artist_name']

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name']