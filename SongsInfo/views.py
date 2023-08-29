from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from .forms import SongForm
from .SongInfoDataManager import SongInfoDataManager
import json


def song_info_result(request):
    return render(
        request,
        "SongsInfo/song-info-result.html",
        {
            "song": {
                "explicit": True,
                "name": "ROCKSTAR (feat. Roddy Ricch)",
                "song_link": "https://open.spotify.com/track/7ytR5pFWmSjzHJIeQkgog4",
                "popularity": 94,
                "duration": "3 minutes 1 seconds",
                "album_data": {
                    "name": "BLAME IT ON BABY",
                    "album-link": "https://open.spotify.com/album/623PL2MBg50Br5dLXC9E9e",
                    "img_link": "https://i.scdn.co/image/ab67616d0000b27320e08c8cc23f404d723b5647",
                    "release_date": "2020-04-17",
                    "total_tracks": 13,
                    "uri": "623PL2MBg50Br5dLXC9E9e"
                },
                "artists_data": [
                    {
                        "name": "DaBaby",
                        "link": "https://open.spotify.com/artist/4r63FhuTkUYltbVAg5TQnk",
                        "uri": "spotify:artist:4r63FhuTkUYltbVAg5TQnk"
                    },
                    {
                        "name": "Roddy Ricch",
                        "link": "https://open.spotify.com/artist/757aE44tKEUQEqRuT6GnEB",
                        "uri": "spotify:artist:757aE44tKEUQEqRuT6GnEB"
                    }
                ]
            }
        }
    )

    # return render(request, "SongsInfo/song-info-result.html", {"song": song})

def songs_select(request):

    return render(
        request,
        "SongsInfo/song-select-list.html",
        {
            "songs": songs["songs"],
        }
    )

@csrf_protect
def song_input_form(request):

    if request.method == "POST":
        print("POST Method")
        form = SongForm(request.POST)

        if form.is_valid():
            print("VALID")
            name = form.cleaned_data["name"]

            DataManager = SongInfoDataManager(name)
            return render(request, "SongsInfo/song-select-list.html", {"songs": DataManager.songs})

        else:
            print("INVALID")

    form = SongForm()
    return render(request, "SongsInfo/song-info-form.html", {'form': form})