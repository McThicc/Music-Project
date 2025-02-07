import datetime

from django.db import models
from django.utils import timezone

class Artist(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    genre_name = models.CharField(max_length=200)
    def __str__(self):
        return self.genre_name

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published")
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)