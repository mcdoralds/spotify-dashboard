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

def get_tracks_by_genre(genre, limit=10, max_tracks=20):
    offset = 0
    all_tracks = []

    while len(all_tracks) < max_tracks:
        results = sp.search(q=f'genre:{genre}', type='track', limit=limit, offset=offset)
        tracks = results['tracks']['items']
        if not tracks:
            break
        all_tracks.extend(tracks)
        offset += limit
        time.sleep(10)  

    return all_tracks[:max_tracks]

def get_track_details(track):
    track_id = track['id']
    track_name = track['name']
    artist_id = track['artists'][0]['id']  # Fetch artist ID
    artist_name = track['artists'][0]['name']
    album_name = track['album']['name']
    release_date = track['album']['release_date']  # Extract release date
    popularity = track['popularity']

    # Fetch audio features
    audio_features = sp.audio_features(track_id)[0]
    if audio_features:
        acousticness = audio_features['acousticness']
        danceability = audio_features['danceability']
        duration_ms = audio_features['duration_ms']
        energy = audio_features['energy']
        instrumentalness = audio_features['instrumentalness']
        loudness = audio_features['loudness']  # Extract loudness
        tempo = audio_features['tempo']
        time_signature = audio_features['time_signature']
        valence = audio_features['valence']
    else:
        acousticness = danceability = duration_ms = energy = instrumentalness = loudness = tempo = time_signature = valence = None
    
    # Fetch genre
    artist_info = sp.artist(artist_id)
    genre = artist_info['genres'][0] if artist_info['genres'] else "Unknown"

    return [track_name, track_id, artist_name, album_name, release_date, popularity, 
            acousticness, danceability, duration_ms, energy, instrumentalness, 
            loudness, tempo, time_signature, valence, genre]

def read_last_processed_genre():
    try:
        with open('last_processed_genre.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def update_last_processed_genre(genre):
    with open('last_processed_genre.txt', 'w') as file:
        file.write(genre)
        
# RUN DA CODE #
def main():
    genres = get_genres()
    last_processed_genre = read_last_processed_genre()

    start_index = genres.index(last_processed_genre) + 1 if last_processed_genre in genres else 0

    columns = ["Track Name", "Track ID", "Artist Name", "Album Name", "Release Date", "Popularity",
               "Acousticness", "Danceability", "Duration (ms)", "Energy", "Instrumentalness",
               "Loudness", "Tempo", "Time Signature", "Valence", "Genre"]

    for genre in genres[start_index:]:
        print(f'Processing genre: {genre}')
        tracks = get_tracks_by_genre(genre)
        data = [get_track_details(track) for track in tracks]

        for track_data in data:  # Correctly placed print statement
            print(track_data)

        df = pd.DataFrame(data, columns=columns)
        with open('spotify_tracks_by_genre.csv', 'a', newline='', encoding='utf-8') as f:
            df.to_csv(f, header=f.tell()==0, index=False)

        update_last_processed_genre(genre)  # Update the last processed genre after successful processing

if __name__ == '__main__':
    main()