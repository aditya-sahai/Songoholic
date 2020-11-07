from django.shortcuts import render


def song_input_form(request):
    return render(request, "SongsInfo/song-info-form.html")