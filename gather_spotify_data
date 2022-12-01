import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
client_id = "c1f74565be774e65aa211462aaf5fed8"
client_secret = "2edce4052f8f46639c0e112658572d66"
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= client_id,client_secret=client_secret))


#Function to extract songs from a playlist: Will run this for all the playlists being added
def extract_songs(playlist):
    if type(playlist) != str: 
        playlist = str(playlist)
        
    playlist_tracks =  spotify.playlist_tracks(playlist)
    tracks = []
    for elem in playlist_tracks['items']:
        tracks.append(elem['track']['external_urls']['spotify'])
    return tracks

#Function to get all scores from feature type for a list of songs
def get_scores(songlist, feature):
    scoreArray = []
    for song in songlist:
        scoreArray.append(spotify.audio_features(song)[0][feature])
    return scoreArray
   
#Function that populates an dictionary where keys are the audio features and values are an array of scores for each song
def populate_song_info(songlist):
    songData = {}
    for elem in songlist:
        songData['danceability'] = get_scores(songlist,'danceability')
        songData['energy'] = get_scores(songlist,'energy')
        songData['speechiness'] = get_scores(songlist,'speechiness')
        songData['acousticness'] = get_scores(songlist,'acousticness')
        songData['instrumentalness'] = get_scores(songlist,'instrumentalness')
        songData['liveness'] = get_scores(songlist,'liveness')
        songData['valence'] = get_scores(songlist,'valence')
    return songData
