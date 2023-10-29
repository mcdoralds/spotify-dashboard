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

#print(client_id, client_secret)

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

    if len(json_result) ==0:
        print ("No artist with that name exists")
        return None
    
    return json_result[0]
    # print(json_result)

### Function to get songs by artist ID
def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url,headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result


token = get_token()
# print(token)
result = search_by_artist(token, "Planet 1999")
artist_id = result["id"]
# print(artist_id)
songs = get_songs_by_artist(token, artist_id)
# print(songs)

for idx, song in enumerate(songs):
    print(f"{idx + 1}.{song['name']}")
