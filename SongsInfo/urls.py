from django.urls import path
from . import views


urlpatterns = [
    path('', views.song_input_form, name="songs-info"),
]
