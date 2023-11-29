# Spotify Data Analysis
NOTE: THE CURRENT PROJECT IS A WIP

### Purpose
The first step is always to determine what questions are being asked, and what hypotheses are being tested. 
For this project, the overarching question was "what cool things can I discover by looking at the data retrievable with the Spotify API?" Some additional questions include:
- Is there a relationship between track features (e.g. valence, tempo, danceability) and song popularity?
- Is there a relationship between other track details (e.g. track title, track artist, track duration) and song popularity?

## Introduction
### Tools
- Spotify Developer API ([Link to Spotify API documentation](https://developer.spotify.com/documentation/web-api))
- Python 3.10
- GPT 4
- Tableau Public
  
## Analysis

### * * * I. Exploratory Analysis * * * 
### Step 1 - Create datasets
This readme details the steps taken to retreive Spotify tracks by genre and analysis of said data. Data is stored in a pandas dataframe and then exported to a csv.

The first step was to write a script to call the Spotify API and retrieve tracks and track details. The script loops through the main genre nodes and retrieves a variable number of tracks per genre. The track details for each track received are recorded into a spreadsheet. 

For this sample dataset, the number of tracks per genre was limited to ~10~ 20. The number of genres appears to be over 100. Spotify's documentation does not specify how the API determines which tracks are returned for each genre. 

~

_**Additional datasets created using a Python script + Spotify's developer API:**_

_- Spotify new releases (albums & singles)_



### Step 2 - Exploratory analysis
#### Excel
Some of the columns needed to be converted and properly formatted before continuing.

![image](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/499f40dc-d24b-4ea8-ba3d-6ef289112d32)

Sorting the dataset by Track ID (unique) revealed that there were some duplicates to be removed. 

![image](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/0fd97307-898b-435c-8ccd-29d67b084781)

### Jupyter Notebook
The csv was then imported into a jupyter notebook for further cleanup and editing.

![4 import to jupyter](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/07a98d17-f63b-43ae-b189-8101bf11c354)
![4 1 view data](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/bb957e86-c372-4e24-b767-3a6fa7d0fd54)
![4 2 format time](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/f2fa7821-8ea2-4a6a-a654-2e7c485a5970)

Once it's confirmed that there are no n/a or blank cells, some basic analysis can be done in the notebook. For example, grouping the data by 'Artist Name' and sorting by the 'Popularity' score shows that there are some artists with multiple releases in the top 100 most popular tracks in the dataset.

![4 3 artists with top 100 popularity](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/ebc8408a-0372-4080-b362-ace6828f0722)

This data can more easily be visualized with a horizontal barchart (numpy, matplotlib) 

![5 top 10 artists](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/62f14fd9-11a9-4cd6-b30d-a01816a4c199)

Tracks can be analyzed by multiple elements and dimensions. In the scatterplot below, the top 100 popular tracks of the dataset are organized by 'Danceability' and 'Polpularity' scores. The size of the dots are determined by 'Tempo' and the colors are based on the 'Energy' score of the tracks. 

![5 7 Danceability by Popularity sized by Tempo colored by energy](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/3642738a-94b8-45bc-bb61-aff3c831dc35)
_See jupyter notebook for additional analyses of the dataset._

### Step 3 - Additional analysis
#### AI Tools
  Chat GPT and other AI tools can be used to do any further analysis or serve as a sanity checks / brainstorming.
  
  ![6 Chat gpt](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/ffe71315-964e-430d-b757-5f7845fedfc0)
  
  The Chat GPT results detail methods already done by the user, but sometimes it's helpful to probe deeper.
  
  ![6 1 Chat gpt](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/5197e172-7e32-44b0-88fa-376cba25c8cf)
  
  This may result in some interesting observations and conclusions.
  
  ![6 2 chat gpt conclusions](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/f2e610c0-559f-4e5c-bd4d-c76fd9a0724d)

#### Collecting More Data
While the first dataset was a good starting place to analyze and visualize Spotify track data, some important and valuable datapoints were not yet captured. Adding 'genre' and 'release_date', and 'loudness' to a lesser degree lends itself to more robust analysis. The number of tracks per genre is also increased to 20, from 10.

see more: "Challenge - API CALL" in section II of this readme

### Step 4 - Visualization & dashboarding
![image](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/c435d16b-cdac-4019-bde0-49c032249513)

The purpose of the visualization below is to see the distribution of track characteristics for the dataset. 
For example, the embedded story below shows that the dataset collected across genres has mostly non-acoustic non-instrumental tracks. 
<div class='tableauPlaceholder' id='viz1701293528772' style='position: relative'><noscript><a href='#'><img alt='Story 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sp&#47;SpotifyData_17008109634340&#47;Story1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='SpotifyData_17008109634340&#47;Story1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sp&#47;SpotifyData_17008109634340&#47;Story1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object>

When a detail, e.g. a Track Name, is selected, the graph displays where that particular track's characteristics fall in relation to other songs.
For example, Fetty Wap's "Trap Queen" has high Energy, Valence, Loudness, and Danceability. It has low Instrumentalness and Acousticness.
![image](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/4b3dcffb-b4b4-40ea-be45-9500a509e8e4)

### * * * II.  * * *
#### Challenge - API CALL
ERROR 429 - Timeout errors when attempting to repeat process with an increased number of tracks collected: 

Even with timeouts written into the script, Error 429 timeouts proved to be a roadblock due. Spotify appears to have a "soft ban" implemented for users with too many 429 errors, which lasts ~15 hours. 
![2 1 api call error](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/b5381544-01b0-42b9-ba0d-fb09e349e5c4)

  #### Solution
  - Increase sleep timer between API calls 
  - Write data to spreadsheet after each genre rather than at the very end
  - To avoid duplicates, create a file to track last genre processed so that the script can start from where it left off if were to crash

  ![image](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/4757a668-d7c0-4f5d-b4f0-49128cf684a7)
  - Print track details 
  ![image](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/80fbf331-3541-466a-ba93-92f22d045d58)


## Results
