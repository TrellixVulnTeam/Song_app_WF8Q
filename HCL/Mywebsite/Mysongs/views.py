from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
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
        return HttpResponseRedirect("/Mysongs/albumdetails")
    else:
        return render(request, 'Mysongs/Createalbum.html')


def albumdetails(request):
    album_list = Albumtable.objects.all()
    return render(request, 'Mysongs/Albumdetails.html', {'album_list': album_list})


def songsview(request, album_id):
    songs_list = Songstable.objects.filter(album_id=album_id)
    return render(request, 'Mysongs/Songsview.html', {'songs_list': songs_list})


def songdetails(request, song_id):
    song_info = Songstable.objects.get(song_id=song_id)
    rating_list = Ratingtable.objects.get(song_id=song_id)





    if len(rating_list) != 0:

        if request.method == 'POST':
            update_inst = Ratingtable.objects.filter(song_id=song_id)[0]
            update_inst.user_rating = request.POST.get('userrating')
            update_inst.save()

            song_info.view_count = song_info.view_count+1
            song_info.save()
            return HttpResponse(song_info)

            #return HttpResponseRedirect('/Mysongs/songsview/songdetails/' + str(song_id))
            #return HttpResponse()
        return render(request, 'Mysongs/Songdetails.html', {'rating': int(rating_list[0].user_rating),
                                                            'song_info': song_info, 'values': [1, 2, 3, 4, 5]})

    elif request.method == 'POST':

        isong = Songstable.objects.get(song_id=song_id)
        iuser = User.objects.get(username=request.user.username)

        irating = Ratingtable()
        irating.song_id = isong
        irating.user_id = iuser
        irating.user_rating = request.POST.get('userrating')
        irating.save()

        song_info.view_count = song_info.view_count+1
        song_info.save()
        return HttpResponse(song_info)


        #return HttpResponseRedirect('/Mysongs/songsview/songdetails/' + str(song_id))

    else:
        return render(request, 'Mysongs/Songdetails.html', {'song_info': song_info},)

