from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View, generic
from django.views.generic import TemplateView
from django.utils import timezone
from .forms import SongForm, GenreForm, AlbumForm, ArtistForm

class PostIndexView(LoginRequiredMixin, TemplateView):
    template_name = "posts/index.html"


class CreateSongView(LoginRequiredMixin, View):
    def get(self, request):
        form = SongForm(request.POST)
        return render(request, "posts/add_song.html", {'form': form})
    def post (self, request):
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.pub_date = timezone.now()
            song.save()
            return redirect('songs:index')
        return render (request, "posts/add_song.html", {'form': form})

class CreateGenreView(LoginRequiredMixin, View):
    def get(self, request):
        form = GenreForm(request.POST)
        return render(request, "posts/add_genre.html", {'form': form})
    def post (self, request):
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save()
            genre.refresh_from_db()
            genre.save()
            return redirect('songs:index')
        return render (request, "posts/add_genre.html", {'form': form})

class CreateAlbumView(LoginRequiredMixin, View):
    def get(self, request):
        form = AlbumForm(request.POST)
        return render(request, "posts/add_album.html", {'form': form})
    def post (self, request):
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.pub_date = timezone.now()
            album.save()
            return redirect('songs:index')
        return render (request, "posts/add_album.html", {'form': form})

class CreateArtistView(LoginRequiredMixin, View):
    def get(self, request):
        form = ArtistForm(request.POST)
        return render(request, "posts/add_artist.html", {'form': form})
    def post (self, request):
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            artist.refresh_from_db()
            artist.save()
            return redirect('songs:index')
        return render (request, "posts/add_artist.html", {'form': form})

