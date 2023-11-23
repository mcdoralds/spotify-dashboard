# Spotify Data Analysis
NOTE: THE CURRENT PROJECT IS A WIP AS OF 20 NOV 2023

### Purpose
The first step is always to determine what questions are being asked, and what hypotheses are being tested. 
For this project, the overarching question was "what cool things can I discover by looking at the data retrievable with the Spotify API?" Some additional questions include:
- a
- s

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

The first step was to write a script to call the Spotify API and retrieve tracks and track details. The script loops through the main genre nodes and retrieves a variable number of tracks per genre. For this sample dataset, the number of tracks per genre was limited to 10.

~

_**Additional datasets created using a Python script + Spotify's developer API:**_

_- Spotify new releases (albums & singles)_



### Step 2 - Exploratory analysis
Some of the columns needed to be converted and properly formatted before continuing.

![image](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/499f40dc-d24b-4ea8-ba3d-6ef289112d32)

Sorting the dataset by Track ID (unique) revealed that there were some duplicates to be removed.

![image](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/4591cfc5-5e94-4775-b07e-fc2e96c3a78a)

950 records remained once duplicates were deleted from the dataset, as shown below.

![image](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/0fd97307-898b-435c-8ccd-29d67b084781)

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
Chat GPT and other AI tools can be used to do any further analysis or serve as a sanity checks / brainstorming.

![6 Chat gpt](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/ffe71315-964e-430d-b757-5f7845fedfc0)

The Chat GPT results more or less detail methods already done by the user, but sometimes it's helpful to probe deeper.

![6 1 Chat gpt](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/5197e172-7e32-44b0-88fa-376cba25c8cf)

This may result in some interesting observations and conclusions.

![6 2 chat gpt conclusions](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/f2e610c0-559f-4e5c-bd4d-c76fd9a0724d)

### Step 4 - Visualization & dashboarding

#### Challenges
ERROR 429 - Timeout errors when attempting to repeat process with an increased number of tracks collected: 

![2 1 api call error](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/b5381544-01b0-42b9-ba0d-fb09e349e5c4)

### * * * II.  * * *
- Include genre as a column
- Record more tracks per genre
- Capture 'loudness' in addition to the other track features
- Get track release date for the dataset
- Write data to spreadsheet after each genre rather than at the very end

## Results
