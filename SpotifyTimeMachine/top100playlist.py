from typing import List, Dict, Any
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()


def setup_spotify_api() -> spotipy.Spotify:
    client_id: str = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret: str = os.getenv("SPOTIFY_CLIENT_SECRET")
    redirect_uri: str = os.getenv("SPOTIFY_REDIRECT_URI")
    scope: str = "playlist-modify-private"

    auth_manager: SpotifyOAuth = SpotifyOAuth(
        client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
    sp: spotipy.Spotify = spotipy.Spotify(auth_manager=auth_manager)
    return sp


def get_user_date_input() -> str:
    date: str = input("Enter the date in yyyy-mm-dd format: ")
    return date


def scrape_billboard_top_100(date: str) -> List[Dict[str, str]]:
    url: str = f"https://www.billboard.com/charts/hot-100/{date}/"
    response: requests.Response = requests.get(url)
    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')

    songs: List[Dict[str, str]] = []
    song_elements = soup.select('li ul li h3.c-title.a-no-trucate')
    artist_elements = soup.select('li ul li span.c-label.a-no-trucate')

    for song_element, artist_element in zip(song_elements, artist_elements):
        song_name: str = song_element.get_text(strip=True)
        artist_name: str = artist_element.get_text(strip=True)
        # Process artist names to exclude features
        processed_artist_name = artist_name.split(' Featuring', 1)[0]
        processed_artist_name = processed_artist_name.split(' featuring', 1)[0]
        processed_artist_name = processed_artist_name.split(' feat', 1)[0]
        processed_artist_name = processed_artist_name.split(' FEAT', 1)[0]

        songs.append({'song': song_name, 'artist': processed_artist_name})

    return songs


def create_spotify_playlist(sp: spotipy.Spotify, date_prettified: str) -> str:
    playlist_name: str = f"Top100-{date_prettified}"
    playlist_description: str = f"Top 100 songs on Billboard as on {date_prettified}."
    user_id: str = os.getenv("SPOTIFY_USER_ID")

    playlist: Dict[str, Any] = sp.user_playlist_create(
        user=user_id, name=playlist_name, public=False, description=playlist_description)

    return playlist['id']


def search_spotify_tracks(sp: spotipy.Spotify, top100_songs: List[Dict[str, str]]) -> List[str]:
    track_ids: List[str] = []
    for song in top100_songs:
        try:
            result = sp.search(
                q=f"track:{song['song']} artist:{song['artist']}", type='track', limit=1, offset=0)
            track_id: str = result['tracks']['items'][0]['id']
            track_ids.append(track_id)
        except IndexError:
            print(
                f"Song '{song['song']}' by '{song['artist']}' not available on Spotify - hence, skipped.")
        except Exception as e:
            print(
                f"An error occurred while searching for '{song['song']}' by '{song['artist']}': {e}")
    return track_ids


def add_tracks_to_playlist(sp: spotipy.Spotify, playlist_id: str, track_ids: List[str]) -> None:
    track_uris = [f'spotify:track:{track_id}' for track_id in track_ids]
    sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)


if __name__ == "__main__":
    date: str = get_user_date_input()
    sp: spotipy.Spotify = setup_spotify_api()
    playlist_id: str = create_spotify_playlist(sp, date)
    track_ids: List[str] = search_spotify_tracks(
        sp, scrape_billboard_top_100(date))
    add_tracks_to_playlist(sp, playlist_id, track_ids)
