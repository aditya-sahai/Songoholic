from django.urls import path
from . import views


urlpatterns = [
    path('', views.song_input_form, name="songs-info"),
    path('result', views.song_info_result, name="songs-info-result"),
    path('select', views.songs_select, name="songs-select"),
]