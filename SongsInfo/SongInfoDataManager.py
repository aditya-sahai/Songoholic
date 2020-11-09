from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json


class SongInfoDataManager:
    def __init__(self, song_name):
        self.get_credentials()

        self.search_song = song_name.lower().strip()
        
        client_credentials_manager = SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        self.get_data()

    def get_credentials(self):
        """Gets the credentials from credentials.json file."""

        credentials = json.load(open("credentials.json"))
        self.client_id = credentials["client_id"]
        self.client_secret = credentials["client_secret"]

    def get_data(self):
        """Gets the data of the given song."""

        search_result = self.sp.search(q=self.search_song, type="track", limit=1)["tracks"]["items"][0]
        artists = search_result["artists"]
        
        artists_data = []
        album_data = {}
        song_data = {}

        for artist in artists:
            name = artist["name"]
            artist_link = artist["external_urls"]["spotify"]
            artists_data.append(
                {
                    "name": name,
                    "link": artist_link,
                }
            )
        
        album_data["name"] = search_result["album"]["name"]
        album_data["album-link"] = search_result["album"]["external_urls"]["spotify"]
        album_data["img-link"] = search_result["album"]["images"][0]["url"]
        album_data["release-date"] = search_result["album"]["release_date"]
        album_data["total-tracks"] = search_result["album"]["total_tracks"]

        song_data["explicit"] = search_result["explicit"]
        song_data["name"] = search_result["name"]
        song_data["song-link"] = search_result["external_urls"]["spotify"]
        song_data["duration"] = round(search_result["duration_ms"] / 60_000, 2)
        song_data["album-data"] = album_data
        song_data["artists-data"] = artists_data

        # print("-" * 90)
        # print(f"\nArtists: {json.dumps(artists_data, indent=4)}")
        # print("-" * 90)
        # print(f"\nAlbum Data: {json.dumps(album_data, indent=4)}")
        print("-" * 90)
        print(f"\nSong Data: {json.dumps(song_data, indent=4)}")
        print("-" * 90)


if __name__ == "__main__":
    Scraper = SongInfoDataManager("rockstar")
