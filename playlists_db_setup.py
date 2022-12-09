from setup import *
import pandas as pd

'''
This was run once to gather the spotify features. Given all the api calls, this process is extremely slow
As a result, we set up the database for comparison beforehand, but this DOES NOT need to be run again.
Only run if you have more songs you want to add to the 'Spotify Playlists.xlsx' file to use for recommendations

'''
def excel_list_to_df():
    '''Create the dataframe from the excel sheet of playlists'''

    df = pd.read_excel("Spotify Playlists 1 per genre.xlsx")
    playlists = df['Link']
    return playlists
    
def export_song_feature_df(df):
    ''
    df.to_excel("spotify_features.xlsx")
    
    

def initialize():
    '''Handles initial setup of the song features we will us for comparison'''

    #Put all playlists in dataframe
    playlists = excel_list_to_df()

    #Create empty array to store all the playlist feature dataframes
    feature_dfs = []
    
    #Iterate through each playlist, convert to songlist dataframe
    for playlist in playlists:
        features = convert_playlist_to_dataframe(playlist)
        feature_dfs.append(features)
    
    #Concatenate dataframes together before export 
    full_frame = pd.concat(feature_dfs,ignore_index=True)

    full_frame.drop_duplicates()

    #export dataframe to excel sheet song_features
    export_song_feature_df(full_frame)


initialize()
    



