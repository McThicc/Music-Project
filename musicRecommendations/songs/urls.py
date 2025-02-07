from django.urls import path

from . import views

app_name = "songs"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("artists/", views.ArtistsIndexView.as_view(), name="artists"),
    path("artists/<int:pk>/", views.ArtistDetailView.as_view(), name="artistdetail"),
    path("<int:song_id>/vote/", views.vote, name="vote"),
]

#pk and song/artist_id are essentially the same thing but they're different enough for me to be scared of messing with the voting system for now