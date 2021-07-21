# This module requires following environment variables!!!
# Create .env in the folder with this file
# And type there environment variables as below
# SPOTIPY_CLIENT_ID = 'your_Spotify_client_id'
# SPOTIPY_CLIENT_SECRET = 'your_Spotify_client_secret'

import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth


class SpotifyPlaylist:
    """  A class to represent Spotify Playlist. """
    def __init__(self, spotipy_client_id, spotipy_client_secret, redirect_uri, scope, cache_path, titles, artists,
                 date):
        """Initialize a Spotify Playlist object."""
        self.spotipy_client_id = os.getenv(spotipy_client_id)  # 'SPOTIPY_CLIENT_ID'
        self.spotipy_client_secret = os.getenv(spotipy_client_secret)  # 'SPOTIPY_CLIENT_SECRET'
        self.redirect_uri = redirect_uri  # "http://example.com"
        self.scope = scope  # 'playlist-modify-public'
        self.cache_path = cache_path  # 'token.txt'
        self.titles = titles
        self.artists = artists
        self.date = date
        load_dotenv()
        self.client = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=self.spotipy_client_id,
                client_secret=self.spotipy_client_secret,
                redirect_uri=redirect_uri,
                scope=self.scope,
                show_dialog=True,
                cache_path=self.cache_path
            ))
        self.user_id = self.client.current_user()['id']
        self.tracks_uris = []

    def check_if_track(self, title, artist, year):
        """ Check if a track may be found in Spotify. """
        # print (f"{index}; '{title}'; {artist}")
        artist = artist.replace(' FEAT. ', '')
        artist = artist.replace(' Feat. ', '')
        artist = artist.split(' & ')
        # artist = artist.split('&')
        single_artist = self.client.search(q=f'track:{title}, artist:{artist}', type='track', limit=1)

        main_artist = self.client.search(q=f'track:{title}, artist:{artist[0]}', type='track', limit=1)
        year_no_artist = self.client.search(q=f'track:{title}, year:{year}', type='track', limit=1)
        no_artist = self.client.search(q=f'track:{title}', type='track', limit=1)
        try:
            multiple_artists = self.client.search(q=f'track:{title}, artist:{artist[0], artist[1]}', type='track',
                                                  limit=1)
            other_artist = self.client.search(q=f'track:{title}, artist:{artist[1]}', type='track', limit=1)
            possible_results = (single_artist, multiple_artists, main_artist, other_artist, year_no_artist, no_artist)
        except IndexError:
            possible_results = (single_artist, main_artist, year_no_artist, no_artist)
        finally:
            for result in possible_results:
                if result['tracks']['items']:
                    break
        return result

    def find_track_uri(self, title, year):
        """ Return uri of the track. """
        index = self.titles.index(title)
        artist = self.artists[index]
        results = self.check_if_track(title, artist, year)
        if results:
            try:
                uri = results['tracks']['items'][0]['uri']
                self.tracks_uris.append(uri)
            except IndexError:
                print(f'{title} by {artist} not found on Spotify. Skipped..')

    def find_tracks_uris(self):
        """ Find the tracks uri-s on Spotify. """
        year = self.date[-4:]
        for title in self.titles:
            self.find_track_uri(title, year)

    def save(self, title):
        """ Save the playlist on the user account using already found uri-s. """
        the_playlist = self.client.user_playlist_create(user=self.user_id,
                                                        name=f'{title} - {self.date}')
        print('The playlist have been created. Have a nice time travel!')
        self.client.playlist_add_items(playlist_id=the_playlist['id'], items=self.tracks_uris)
