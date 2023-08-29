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

        credentials = json.load(open("SongsInfo/credentials.json"))
        self.client_id = credentials["client_id"]
        self.client_secret = credentials["client_secret"]

    def get_data(self):
        """Gets the data of the given song."""

        search_results = self.sp.search(q=self.search_song, type="track")["tracks"]["items"]
        with open("temp.json", "w") as f:
            json.dump(self.sp.search(q=self.search_song[0], type="track"), f, indent=4)
        self.songs = []

        for search_result in search_results:
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
                        "uri": artist["uri"]
                    }
                )

            album_data["name"] = search_result["album"]["name"]
            album_data["album-link"] = search_result["album"]["external_urls"]["spotify"]
            album_data["img_link"] = search_result["album"]["images"][0]["url"]
            album_data["release_date"] = search_result["album"]["release_date"]
            album_data["total_tracks"] = search_result["album"]["total_tracks"]
            album_data["uri"] = search_result["album"]["uri"].split(":")[2]

            song_data["explicit"] = search_result["explicit"]
            song_data["name"] = search_result["name"]
            song_data["song_link"] = search_result["external_urls"]["spotify"]
            total_seconds = search_result["duration_ms"] // 1000
            song_data["popularity"] = search_result["popularity"]
            minutes = total_seconds // 60
            seconds = total_seconds - minutes * 60
            song_data["duration"] = f"{minutes} minutes {seconds} seconds"
            song_data["album_data"] = album_data
            song_data["artists_data"] = artists_data

            # print("-" * 90)
            # print(f"\nArtists: {json.dumps(artists_data, indent=4)}")
            # print("-" * 90)
            # print(f"\nAlbum Data: {json.dumps(album_data, indent=4)}")
            # print("-" * 90)
            # print(f"\nSong Data: {json.dumps(song_data, indent=4)}")
            # print("-" * 90)
            self.songs.append(song_data)
        
        # with open("SongsInfo/temp.json", "w") as f:
        #     json.dump(self.songs[0], f, indent=4)


if __name__ == "__main__":
    song = input("Enter Song\n>>>")
    Scraper = SongInfoDataManager(song)
