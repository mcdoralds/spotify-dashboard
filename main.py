from dotenv import load_dotenv
import os
import base64
import json
import requests
from requests import post, get

### File Path for .env file
dotenv_path = r'J:\Documents\Projects\Spotify Dashboard\spotify-dashboard.env'
load_dotenv(dotenv_path) 

# Get CLIENT_ID and CLIENT_SECRET from environment variables from Spotify Dev Dashboard
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

### Function to get Spotify access token
def get_token():
    auth_string = client_id + ":" + client_secret # create authorization string 
    auth_bytes = auth_string.encode("utf-8") # encodes authorization string with base64
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8") #convert base64 object to string

    url = "https://accounts.spotify.com/api/token" # defines URL for the Spotify token endpoint

    ## Headers for POST request
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"} # defines data to send to POST request
    result= post(url, headers=headers, data=data) # makes POST request to get Spotify token
    json_result = json.loads(result.content) # parses JSON response
    token = json_result["access_token"] # extracts access token from JSON response
    return token

### Function to create headers for auth requests
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


### Function to search artist details by artist name
def search_by_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"] # parses JSON response

    if len(json_result) == 0:
        print ("No artist with that name exists")
        return None
    
    return json_result[0]

### Function to get songs by artist ID
def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url,headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

### Function to get all albums and singles released to Spotify in 2023
def get_new_albums_2023(token):
    # Define the query parameters to filter new albums in 2023
    country = "US"  # Selects the country code 
    limit = 10  # Adjusts the number of new albums to retrieve
    offset = 0
    year = 2023

    url = "https://api.spotify.com/v1/browse/new-releases"
    headers = get_auth_header(token)
    query = f"?country={country}&limit={limit}&offset={offset}&year={year}&album_type=album"

    query_url = url + query
    result = get(query_url, headers=headers)
    
    if result.status_code == 200:
        json_result = result.json()
        return json_result["albums"]["items"]  # Parses JSON response for albums

### Function to get artist details by artist ID
def get_artist_details(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = get_auth_header(token)

    result = get(url, headers=headers)

    if result.status_code == 200:
        artist_info = result.json()
        return artist_info
    else:
        print(f"Failed to get details for artist {artist_id} - Status Code: {result.status_code}")
        return None

### Function to get album/single details by album ID
def get_album_info(token, album_id):
    url = f"https://api.spotify.com/v1/albums/{album_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)

    if result.status_code == 200:
        album_info = result.json()
        return album_info
    else:
        print(f"Failed to get album info for album ID {album_id} - Status Code: {result.status_code}")
        return None

### RUN DA PROGRAM ###
token = get_token()

new_albums_2023 = get_new_albums_2023(token)
for idx, album in enumerate(new_albums_2023):
    # Extract relevant information
    album_name = album["name"]
    artist_id = album["artists"][0]["id"]  # Assuming the first artist in the list
    release_date = album["release_date"]
    track_number = album.get("total_tracks", "N/A")
    album_type = album.get("album_type", "N/A")

    artist_info = get_artist_details(token, artist_id)
    if artist_info:
        genres = ", ".join(artist_info.get("genres", ["N/A"]))
        album_id = album["id"]
        album_info = get_album_info(token, album_id)


    if album_info:
        album_popularity = album_info["popularity"]
        album_label = album_info["label"]
        album_images = album_info["images"]

    result = f"Artist Name: {artist_info['name']} - Album Type: {album_type} - Album/Single Name: {album_name} - Total Tracks: {track_number} - Release Date: {release_date} - Genre(s): {genres} - Album Popularity: {album_popularity} - Album Label: {album_label}"

    print(f"{idx + 1}. {result}")