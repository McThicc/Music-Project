from django.db.models import F
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader #Could theoretically remove but I'm keeping it to remember I can render each URL this way
from django.urls import reverse
from django.views import generic

from .models import Song, Artist

#ListView vs. DetailView
#DetailView - self.object contains the object the view is working on and gets certain methods and attributes
#ListView - self.object_list contains the list of objects the view is working on and gets different methods and attributes

class IndexView(generic.ListView):
    template_name = "songs/index.html"
    context_object_name = "latest_song_list"

    def get_queryset(self):
        """Return the last five published songs."""
        return Song.objects.order_by("-pub_date")[:5]
    
class ArtistsIndexView(generic.ListView):
    template_name = "songs/artists.html"
    context_object_name = "latest_artist_list"

    def get_queryset(self):
        """Return the last five published artists."""
        return Artist.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Song
    template_name = "songs/detail.html"

class ArtistDetailView(generic.DetailView):
    model = Artist
    template_name = "songs/artistdetail.html"

#The other views also used to look like this but as I was learning more, the above generic method is better abstracted
def vote(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    try:
         selected_choice = song
    except (KeyError, Song.DoesNotExist):
         return render(request, "songs/detail.html", {"song": song, "error_message": "You didn't do it right dumbass",},)
    else:
         selected_choice.votes = F("votes") + 1
         selected_choice.save()
    return HttpResponseRedirect(reverse("songs:detail", args=(song.id,)))