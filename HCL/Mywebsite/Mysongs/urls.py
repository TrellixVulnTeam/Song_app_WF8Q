from django.urls import path
from .import views


urlpatterns = [
    path('songsview/songdetails/<int:song_id>', views.songdetails, name='Songdetail'),
    path('songsview/<int:album_id>', views.songsview, name='Songs'),
    path('albumdetails', views.albumdetails, name='Album'),
    path('createalbum', views.createalbum, name='Home'),
]