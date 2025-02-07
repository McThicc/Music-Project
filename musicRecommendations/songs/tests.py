import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Song

#tutorial basic bitch type test shit fr
class SongModelTests(TestCase):
    def test_future_proof(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_song = Song(pub_date=time)
        self.assertIs(future_song.was_published_recently(), False)
    def test_grandfather_paradox(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_song = Song(pub_date=time)
        self.assertIs(old_song.was_published_recently(), False)
    def test_recency_bias(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_song = Song(pub_date=time)
        self.assertIs(recent_song.was_published_recently(), True)

#to do: make some of your own tests