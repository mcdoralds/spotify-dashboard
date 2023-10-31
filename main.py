from dotenv import load_dotenv
import os
import base64
import json
import requests
import time
import pandas as pd 


# Load environment variables from .env file
dotenv_path = r'J:\Documents\Projects\Spotify Dashboard\spotify-dashboard\.env'
load_dotenv(dotenv_path)

# Get CLIENT_ID and CLIENT_SECRET from environment variables from Spotify Dev Dashboard
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    # Create authorization string
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")  # Convert base64 object to string

    url = "https://accounts.spotify.com/api/token"  # Define URL for the Spotify token endpoint

    # Headers for POST request
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}  # Define data to send in the POST request
    result = requests.post(url, headers=headers, data=data)  # Make a POST request to get the Spotify token
    json_result = result.json()  # Parse JSON response
    token = json_result["access_token"]  # Extract access token from JSON response
    return token

def get_auth_header(token):
    return {"Authorization": f"Bearer {token}"}


def retry_on_429(max_retries=5, retry_delay=5):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.HTTPError as e:
                    if e.response.status_code == 429:
                        print(f"Rate limited. Waiting for {retry_delay} seconds...")
                        time.sleep(retry_delay)
                        retries += 1
                    else:
                        raise  # Re-raise the exception if it's not a 429 error
            raise Exception("Reached max retries")
        return wrapper
    return decorator


def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url + query
    result = requests.get(query_url, headers=headers)
    json_result = result.json()["artists"]["items"]  # Parse JSON response

    if not json_result:
        print("No artist with that name exists")
        return None
    
    return json_result[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = requests.get(url, headers=headers)
    json_result = result.json()["tracks"]
    return json_result

def get_new_albums_2023(token, country="US", limit=10, offset=0):
    year = 2023
    all_albums = []

    while True:
        url = "https://api.spotify.com/v1/browse/new-releases"
        headers = get_auth_header(token)
        query = f"?country={country}&limit={limit}&offset={offset}&year={year}&album_type=album"
        query_url = url + query
        result = requests.get(query_url, headers=headers)
        
        if result.status_code == 200:
            json_result = result.json()
            albums = json_result["albums"]["items"]
            if not albums:
                break
            all_albums.extend(albums)
            offset += limit
        else:
            print(f"Failed to retrieve albums - Status Code: {result.status_code}")
            break

    return all_albums

def get_album_info(token, album_id):
    url = f"https://api.spotify.com/v1/albums/{album_id}"
    headers = get_auth_header(token)
    result = requests.get(url, headers=headers)

    if result.status_code == 200:
        album_info = result.json()
        return album_info
    else:
        print(f"Failed to get album info for album ID {album_id} - Status Code: {result.status_code}")
        return None

@retry_on_429(max_retries=5, retry_delay=5)
def get_artist_details(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = get_auth_header(token)
    result = requests.get(url, headers=headers)
    if result.status_code == 200:
        artist_info = result.json()
        return artist_info
    else:
        raise requests.exceptions.HTTPError(response=result)


def print_album_details(idx, album_info, artist_info):
    album_name = album_info["name"]
    album_type = album_info.get("album_type", "N/A")
    release_date = album_info["release_date"]
    track_number = album_info.get("total_tracks", "N/A")
    genres = ", ".join(artist_info.get("genres", ["N/A"]))
    
    album_id = album_info["id"]
    album_info = get_album_info(token, album_id)
    
    if album_info:
        album_popularity = album_info["popularity"]
        album_label = album_info["label"]
        album_images = album_info["images"]
        
        result = f"Artist Name: {artist_info['name']} - Album Type: {album_type} - Album/Single Name: {album_name} - Total Tracks: {track_number} - Release Date: {release_date} - Genre(s): {genres} - Album Popularity: {album_popularity} - Album Label: {album_label}"
    else:
        result = f"Artist Name: {artist_info['name']} - Album Type: {album_type} - Album/Single Name: {album_name} - Total Tracks: {track_number} - Release Date: {release_date} - Genre(s): {genres}"

    print(f"{idx + 1}. {result}")

# RUN DA PROGRAM
csv_filename = r'J:\Documents\Projects\Spotify Dashboard\spotify-dashboard\spotify_albums.csv'
token = get_token()
items_per_page = 10
offset = 0
offset_threshold = 90
record_number = 0

# Create an empty list to store the data
data = []

record_count = 0  # Counter to keep track of the number of records printed

# Create an empty set to store processed album IDs
processed_albums = set()

while True:
    new_albums_2023 = get_new_albums_2023(token, limit=items_per_page, offset=offset)
    if not new_albums_2023:
        break

    for idx, album in enumerate(new_albums_2023):
        album_id = album["id"]  # Assuming the album ID is unique

        # Check if the album ID is already in the set of processed albums
        if album_id in processed_albums:
            print(f"Duplicate album found: {album_id}")
            break

        processed_albums.add(album_id)  # Add the album ID to the set of processed albums

        artist_id = album["artists"][0]["id"]  # Assuming the first artist in the list
        artist_info = get_artist_details(token, artist_id)

        if artist_info:
            # Extract information as you did before
            artist_name = artist_info["name"]
            album_name = album["name"]
            album_type = album.get("album_type", "N/A")
            release_date = album["release_date"]
            track_number = album.get("total_tracks", "N/A")
            genres = ", ".join(artist_info.get("genres", ["N/A"]))

            album_info = get_album_info(token, album_id)  # Use the album_id here
            album_popularity = album_info.get("popularity", "N/A")
            album_label = album_info.get("label", "N/A")

            # Append the data to the list
            data.append([record_number, artist_name, album_type, album_name, track_number, release_date, genres, album_popularity, album_label])

            # Print the data being added to 'data'
            print(f"Data added to 'data': {data[-1]}")

            record_number += 1

            # Check if offset should be increased
            if record_number % offset_threshold == 0:
                offset += items_per_page

    if album_id in processed_albums:
        break  # Exit the main loop if a duplicate is found

# Create a DataFrame from the list of data
df = pd.DataFrame(data, columns=["Record Number", "Artist Name", "Album Type", "Album/Single Name", "Total Tracks", "Release Date", "Genre", "Album Popularity", "Album Label"])

# Write the DataFrame to a CSV file
df.to_csv(csv_filename, index=False)