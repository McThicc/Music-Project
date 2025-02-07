import datetime

from django.db import models
from django.utils import timezone

#The model for Artist is also bare bones (If you're reading this top-down that doesn't make sense LOL) but I'm not entirely sure what I'm going to do with it yet, maybe tie it to an account run by the artist?
class Artist(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    def __str__(self):
        return self.name

#The Genre model is kind of bare bones right now but once I actually start working on the recommendation side of this app, I feel like it will come very much in handy
class Genre(models.Model):
    genre_name = models.CharField(max_length=200)
    def __str__(self):
        return self.genre_name

#The model for a song contains its title, artist, genre, and number of votes it has
#As well as the pub date
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