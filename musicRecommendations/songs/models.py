import datetime
import requests
from decouple import config
from django.db import models
from django.utils import timezone

#The model for Artist is also bare bones (If you're reading this top-down that doesn't make sense LOL) but I'm not entirely sure what I'm going to do with it yet, maybe tie it to an account run by the artist?
class Artist(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    image_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.image_url:
            self.fetch_artist_image()
        super().save(*args, **kwargs)
        
    def fetch_artist_image(self):
        api_key = config('LAST_FM_API_KEY')
        url = f'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={self.name}&api_key={api_key}&format=json'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'artist' in data and 'image' in data['artist']:
                images = data['artist']['image']
                if images:
                    self.image_url = images[-1]['#text']

#The Genre model is kind of bare bones right now but once I actually start working on the recommendation side of this app, I feel like it will come very much in handy
class Genre(models.Model):
    genre_name = models.CharField(max_length=200)

    def __str__(self):
        return self.genre_name


class Album(models.Model):
    album_name = models.CharField(max_length=200)
    artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published")
    image_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.album_name
    
    def save(self, *args, **kwargs):
        if not self.image_url:
            self.fetch_album_image()
        super().save(*args, **kwargs)

    def fetch_album_image(self): #I removed the printing of the data in this function because it seems to be working and I don't need it
        api_key = config('LAST_FM_API_KEY')
        url = f'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={api_key}&artist={self.artist_name}&album={self.album_name}&format=json'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'album' in data and 'image' in data['album']:
                images = data['album']['image']
                if images:
                    self.image_url = images[-1]['#text']
                    self.save()

#The model for a song contains its title, artist, genre, and number of votes it has
#As well as the pub date
class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    featured_artists = models.ManyToManyField(Artist, related_name='featured_artists', blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published")
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now