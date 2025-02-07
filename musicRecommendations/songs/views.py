from django.db.models import F
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader #Could theoretically remove but I'm keeping it to remember I can render each URL this way
from django.urls import reverse
from .models import Song, Artist

def index(request):
    latest_song_list = Song.objects.order_by("-pub_date")[:5]
    context = {
        "latest_song_list": latest_song_list,
    }
    return render(request, "songs/index.html", context)

def results(request, song_id):
    return HttpResponse("You're looking at song %s." % song_id)

def detail(request, song_id):
        song = get_object_or_404(Song, pk=song_id)
        return render(request, "songs/detail.html", {"song": song})

def artists(request):
    latest_artist_list = Artist.objects.order_by("-pub_date")[:5]
    context = {
        "latest_artist_list": latest_artist_list,
    }
    return render(request, "songs/artists.html", context)

def artistdetail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, "songs/artistdetail.html", {"artist": artist})

def vote(request, song_id):
    return HttpResponse("You're voting on song %s" % song_id)