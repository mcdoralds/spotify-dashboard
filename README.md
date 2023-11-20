# Spotify Data Analysis
## Introduction
### Tools
- Spotify Developer API ([Link to Spotify API documentation](https://developer.spotify.com/documentation/web-api))
- Python 3.10
- GPT 4
  
## Analysis
### Step 1 - Create datasets
The first step was to write a script to call the Spotify API and retrieve tracks and track details.

Datasets created:
- Spotify new releases (albums & singles)
- Spotify tracks by genre

### Step 2 - Exploratory analysis
Some of the columns needed to be converted and properly formatted before continuing.

![image](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/757a6ee5-a3d1-4f04-a2ef-d02c4efd6762)

Sorting the dataset by Track ID (unique) revealed that there were some duplicates to be removed.

![image](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/c72f63d0-cf56-47ba-8355-2027e4701537)

950 records remained once duplicates were deleted from the dataset, as shown below.

![image](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/6ee04b29-9992-4070-8362-b56ceee83f4f)

The csv was then imported into a jupyter notebook for further cleanup.

![image](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/ad757854-8236-4201-ad38-11d62c5fb557)
![image](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/0970f3f4-5879-44b0-8912-139c31635c30)
![image](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/aac12d41-a5b2-469c-b234-aad1a5d8be74)

Once it's confirmed that there are no n/a or blank cells, some basic analysis can be done in the notebook. For example, grouping the data by 'Artist Name' and sorting by the'Popularity' score shows that there are some artists with multiple releases in the top 100 most popular tracks in the dataset.

![4 3 artists with top 100 popularity](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/85506cb4-f00c-4d9f-8662-4e5fcbd89951)

This data can more easily be visualized with a horizontal barchart (numpy, matplotlib) 

![5 top 10 artists](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/2cd8095b-dade-49f0-b86b-c2607a1e8b82)

Tracks can be analyzed by multiple elements. In the scatterplot below, the top 100 popular tracks of the dataset are organized by 'Danceability' and 'Polpularity' scores. The size of the dots are determined by 'Tempo' and the colors are based on the 'Energy' score of the tracks. 

![5 7 Danceability by Popularity sized by Tempo colored by energy](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/f24a442f-d063-4e03-b891-6dcf8d73ff54)
_See jupyter notebook for additional analyses of the dataset._

### Step 3 - Additional analysis
Chat GPT and other AI tools can be used to do any further analysis or serve as a sanity checks / brainstorming.

![6 Chat gpt](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/7fd37d27-dc51-4861-bfde-ef8768d33914)

The Chat GPT results more or less detail methods already done by the user, but sometimes it's helpful to probe deeper.

![6 1 Chat gpt](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/0eaac15b-17e9-472a-8e9c-075d22268c0c)

This may result in some interesting observations and conclusions.

![6 2 chat gpt conclusions](https://github.com/mcdoralds/spotify-dashboard/assets/31219195/18604233-676c-432d-a768-c37e29683023)

### Step 4 - Visualization & dashboarding

## Results
