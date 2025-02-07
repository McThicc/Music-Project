from django.urls import path

from . import views

app_name = "songs"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:song_id>/", views.detail, name="detail"),
    path("artists/", views.artists, name="artists"),
    path("artists/<int:artist_id>/", views.artistdetail, name="artistdetail"),
    path("<int:song_id>/results/", views.results, name="results"),
    path("<int:song_id>/vote/", views.vote, name="vote"),
]