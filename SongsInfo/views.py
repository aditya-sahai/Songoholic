from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from SongsInfo.models import Song
from .forms import SongForm
import json


def song_info_result(request):
    return render(
        request,
        "SongsInfo/song-info-result.html",
        {
            "song": {
                "explicit": True,
                "name": "Radioactive",
                "song_link": "https://open.spotify.com/track/69yfbpvmkIaB10msnKT7Q5",
                "popularity": 71,
                "duration": "4 minutes 36 seconds",
                "album_data": {
                    "name": "Radioactive",
                    "album-link": "https://open.spotify.com/album/2M0IZTKgkN3ZpYluF4lKAM",
                    "img_link": "https://i.scdn.co/image/ab67616d0000b273d8941843ba4d684f76a94956",
                    "release_date": "2014-01-01",
                    "total_tracks": 1,
                    "uri": "2M0IZTKgkN3ZpYluF4lKAM"
                },
                "artists_data": [
                    {
                        "name": "Imagine Dragons",
                        "link": "https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q",
                        "uri": "spotify:artist:53XhwfbYqKCa1cC15pYq2q"
                    },
                    {
                        "name": "Kendrick Lamar",
                        "link": "https://open.spotify.com/artist/2YZyLoL8N0Wb9xBt1NhZWg",
                        "uri": "spotify:artist:2YZyLoL8N0Wb9xBt1NhZWg"
                    }
                ]
            }
        }
    )

def songs_select(request):
    with open("SongsInfo/temp.json", "r") as f:
        data = json.load(f)
    return render(
        request,
        "SongsInfo/song-select-list.html",
        {
            "songs": data,
        }
    )

@csrf_protect
def song_input_form(request):

    if request.method == "POST":
        form = SongForm(request.POST)
        print(form)

        if form.is_valid():
            print("\n\nVALID\n")
            post = form.save(commit=False)
            post.save()
            return redirect("/songs-info/result", name=form)
        
        else:
            print("\n\nINVALID\n")
            print(f"\n{form.errors}\n")

    else:
        form = SongForm()

    return render(request, "SongsInfo/song-info-form.html")