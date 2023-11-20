import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import os
from dotenv import load_dotenv

# Load environment variables
dotenv_path = r'J:\Documents\Projects\Spotify Dashboard\spotify-dashboard\.env'
load_dotenv(dotenv_path)

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Spotify API Authentication
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)


# FUNCTIONS #
def get_genres():
    return sp.recommendation_genre_seeds()['genres']

def get_tracks_by_genre(genre, limit=10, max_tracks=1):
    offset = 0
    all_tracks = []

    while len(all_tracks) < max_tracks:
        results = sp.search(q=f'genre:{genre}', type='track', limit=limit, offset=offset)
        tracks = results['tracks']['items']
        if not tracks:
            break
        all_tracks.extend(tracks)
        offset += limit
        time.sleep(31)  

    return all_tracks[:max_tracks]

def get_track_details(track):
    track_id = track['id']
    track_name = track['name']
    artist_name = track['artists'][0]['name']
    album_name = track['album']['name']
    popularity = track['popularity']

    audio_features = sp.audio_features(track_id)[0]
    if audio_features:
        acousticness = audio_features['acousticness']
        danceability = audio_features['danceability']
        duration_ms = audio_features['duration_ms']
        energy = audio_features['energy']
        instrumentalness = audio_features['instrumentalness']
        tempo = audio_features['tempo']
        time_signature = audio_features['time_signature']
        valence = audio_features['valence']
    else:
        acousticness = danceability = duration_ms = energy = instrumentalness = tempo = time_signature = valence = None

    return [track_name, track_id, artist_name, album_name, popularity, acousticness, danceability, duration_ms, energy, instrumentalness, tempo, time_signature, valence]

# RUN DA CODE #
def main():
    genres = get_genres()
    data = []

    for genre in genres:
        print(f'Processing genre: {genre}')
        tracks = get_tracks_by_genre(genre)
        for track in tracks:
            track_data = get_track_details(track)
            data.append(track_data)

    columns = ["Track Name", "Track ID", "Artist Name", "Album Name", "Popularity",
               "Acousticness", "Danceability", "Duration (ms)", "Energy", "Instrumentalness",
               "Tempo", "Time Signature", "Valence"]

    df = pd.DataFrame(data, columns=columns)
    df.to_csv('spotify_tracks_by_genre.csv', index=False)

if __name__ == '__main__':
    main()

