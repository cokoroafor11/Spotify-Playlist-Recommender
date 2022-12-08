import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
client_id = "c1f74565be774e65aa211462aaf5fed8"
client_secret = "2edce4052f8f46639c0e112658572d66"
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= client_id,client_secret=client_secret),requests_timeout=10000,retries=10)






def extract_songs(playlist):
    '''Function to extract songs from a playlist: Will run this for all the playlists being added'''

    if type(playlist) != str: 
        playlist = str(playlist)
        
    playlist_tracks =  spotify.playlist_tracks(playlist)
    tracks = []
    for elem in playlist_tracks['items']:
        try:
            tracks.append(elem['track']['external_urls']['spotify'])
        except TypeError:
            pass
    return tracks



def get_scores(song, feature):
    '''Function to get score for feature type of a song'''
    feature_score = 0
    try:
        feature_score = spotify.audio_features(song)[0][feature]
    except TypeError:
        feature_score = 0
        pass
    return feature_score
   
def convert_playlist_to_dataframe(playlist):
    '''Convert a playlist of songs to a dataframe'''
    songlist = extract_songs(playlist)
    song_data = populate_song_info(songlist)
    df = pd.DataFrame(song_data)
    return df

def populate_song_info(songlist):
    '''
    Function that populates an dictionary where keys are the audio features and values are an array of scores for each song
    This function performs the lionshare of data setup
    '''
    #Storage for various types of data
    song_data = {}
    name_array = []
    dance_array = []
    energy_array = []
    speech_array = []
    acoustic_array = []
    instrument_array = []
    live_array = []
    valence_array = []
    link_array = []
    
    #Loop to append song info to appropriate array
    for song in songlist:
        name_array.append(get_track_name(song))
        dance_array.append(get_scores(song,'danceability'))
        energy_array.append(get_scores(song,'energy'))
        speech_array.append(get_scores(song,'speechiness'))
        acoustic_array.append(get_scores(song,'acousticness'))
        instrument_array.append(get_scores(song,'instrumentalness'))
        live_array.append(get_scores(song,'liveness'))
        valence_array.append(get_scores(song,'valence'))
        link_array.append(song)
    
    #Put all song data in a library with proper labels
    song_data['Track Name'] = name_array
    song_data['danceability'] = dance_array
    song_data['energy'] = energy_array
    song_data['speechiness'] = speech_array
    song_data['acousticness'] = acoustic_array
    song_data['instrumentalness'] = instrument_array
    song_data['liveness'] = live_array
    song_data['valence'] = valence_array
    song_data['link'] = link_array
    
    return song_data


def get_track_artists(track):
    '''Get all artists for each track'''

    artists = []
    for artist in spotify.track(track)['artists']:
        artists.append(artist['name'])
    return artists


def get_track_name(track):
    '''Get track name'''

    return spotify.track(track)['name']

