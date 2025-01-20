import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

# Initialize Spotify OAuth
sp_oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="playlist-modify-public"
)

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=sp_oauth)

def create_playlist_and_add_songs(songs, user_id, music_date):
    # Create a new playlist with the date in the name
    playlist = sp.user_playlist_create(user=user_id, name=f"Billboard Hot 100 on {music_date}", public=True)
    playlist_id = playlist['id']

    # Search for each song and add to the playlist
    for song in songs:
        query = f"{song['title']} {song['singer']}"
        result = sp.search(q=query, type="track", limit=1)
        tracks = result['tracks']['items']
        if tracks:
            track_id = tracks[0]['id']
            sp.playlist_add_items(playlist_id, [track_id])
