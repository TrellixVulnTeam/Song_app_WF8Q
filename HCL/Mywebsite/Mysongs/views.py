from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Albumtable, Songstable, Ratingtable


def createalbum(request):

    if request.method == 'POST':
        recordexists = Albumtable.objects.filter(album_name=request.POST.get('albumname'))
        if not recordexists:
            ialbum = Albumtable()
            ialbum.album_name = request.POST.get('albumname')
            ialbum.album_year = request.POST['albumyear']
            ialbum.save()
        else:
            ialbum = Albumtable(album_id=recordexists[0].album_id)

        isongs = Songstable()
        isongs.album_id = ialbum
        isongs.song_name = request.POST.get('songname')
        isongs.artist_name = request.POST.get('artistname')
        isongs.save()
        #return HttpResponseRedirect("/Mysongs/Songselection")
        return HttpResponseRedirect("/Mysongs/albumdetails")
    else:
        #newrecord = Songstable.objects.get(song_id=7)
        #matching_album = newrecord.album_id.album_name
        #return HttpResponse(matching_album)
        return render(request, 'Mysongs/Createalbum.html')


def albumdetails(request):
    album_list = Albumtable.objects.all()
    return render(request, 'Mysongs/Albumdetails.html', {'album_list': album_list})


def songsview(request,album_id):
    songs_list = Songstable.objects.filter(album_id=album_id)
    return render(request, 'Mysongs/Songsview.html', {'songs_list': songs_list})
    #return HttpResponse(songs_list)


def songdetails(request,song_id):

    song_info = Songstable.objects.filter(song_id=song_id)
    rating_list = Ratingtable.objects.filter(song_id=song_id)

    if len(rating_list) != 0:

        if request.method == 'POST':
            update_inst = Ratingtable.objects.filter(song_id=song_id)[0]
            update_inst.user_rating = request.POST.get('userrating')
            update_inst.save()
            return HttpResponseRedirect('/Mysongs/songsview/songdetails/' + str(song_id))
        return render(request, 'Mysongs/Songdetails.html', {'rating': int(rating_list[0].user_rating),
                                                            'song_info': song_info, 'values': [1, 2, 3, 4, 5]})
    elif request.method == 'POST':

        isong = Songstable.objects.get(song_id=song_id)  # Song table instance
        iuser = User.objects.get(username=request.user.username)  # User table instance, filtered by username

        irating = Ratingtable()  # Rating table instance
        irating.song_id = isong  # Adding values to the columns in Ratings table
        irating.user_id = iuser
        irating.user_rating = request.POST.get('userrating')
        irating.save()  # Save rows
        return HttpResponseRedirect('/Mysongs/songsview/songdetails/' + str(song_id))

    else:
        return render(request, 'Mysongs/Songdetails.html', {'song_info': song_info})

