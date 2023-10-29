from dotenv import load_dotenv
import os
import base64
import json
from requests import post

### File Path for .env file
dotenv_path = r'J:\Documents\Projects\Spotify Dashboard\.env'
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

token = get_token()
# print(token)