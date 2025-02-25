from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path("", views.PostIndexView.as_view(), name="post_index"),
    path('add_song/', views.CreateSongView.as_view(), name='add_song'),
    path('add_genre/', views.CreateGenreView.as_view(), name='add_genre'),
    path('add_album/', views.CreateAlbumView.as_view(), name='add_album'),
    path('add_artist/', views.CreateArtistView.as_view(), name='add_artist'),
]