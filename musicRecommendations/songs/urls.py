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
