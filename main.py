from setup import *
import pandas as pd
import numpy as np

def excel_list_to_df():
    ##Create the dataframe from the excel sheet of playlists
    df = pd.read_excel("Spotify Playlists.xlsx")
    playlists = df['Link']
    return playlists
    
def convert_playlist_to_dataframe(playlist):
    songlist = extract_songs(playlist)
    song_data = populate_song_info(songlist)
    df = pd.Dataframe(song_data)
    return df

def get_user_playlist(): 
    good_input = False
    user_playlist = ''
    user_songs = []
    user_playlist = str(input("Please enter a playlist"))
    #If input is not a url: return false
    #If input is a url but for a song rather than a playlist
    #Else set good input to true
        
    
    user_songs = convert_playlist_to_dataframe(user_playlist)
    return user_songs

def get_user_statistics(song_features):
    averages = {}
    variances = {}
    avg_danceability = np.mean(song_features['danceability'])
    var_danceability = np.var(song_features['danceability'])

    avg_energy = np.mean(song_features['energy'])
    var_energy = np.var(song_features['energy'])

    avg_speechiness = np.mean(song_features['speechiness'])
    var_speechiness = np.var(song_features['speechiness'])

    avg_acousticness = np.mean(song_features['acousticness'])
    var_acousticness = np.var(song_features['acousticness'])

    avg_instrumentalness = np.mean(song_features['instrumentalness'])
    var_instrumentalness = np.var(song_features['instrumentalness'])

    avg_liveness = np.mean(song_features['liveness'])
    var_liveness = np.var(song_features['liveness'])

    avg_valence = np.mean(song_features['valence'])
    var_valence = np.var(song_features['valence'])

    averages['danceability'] = avg_danceability
    averages['energy'] = avg_energy
    averages['speechiness'] = avg_speechiness
    averages['acousticness'] = avg_acousticness
    averages['instrumentalness'] = avg_instrumentalness
    averages['liveness'] = avg_liveness
    averages['valence'] = avg_valence

    variances['danceability'] = var_danceability
    variances['energy'] = var_energy
    variances['speechiness'] = var_speechiness
    variances['acousticness'] = var_acousticness
    variances['instrumentalness'] = var_instrumentalness
    variances['liveness'] = var_liveness
    variances['valence'] = var_valence

    return (averages,variances)

def compare_features(avg,var,song_features):
    arr = []
    feature = 'danceability'
    if song_features[feature] >= avg[feature]-var[feature] and song_features[feature] <= avg[feature]+var[feature]:
        arr.append(feature)         

    feature = 'energy'
    if song_features[feature] >= avg[feature]-var[feature] and song_features[feature] <= avg[feature]+var[feature]:
        arr.append(feature)

    feature = 'speechiness'
    if song_features[feature] >= avg[feature]-var[feature] and song_features[feature] <= avg[feature]+var[feature]:
        arr.append(feature)

    feature = 'acousticness'
    if song_features[feature] >= avg[feature]-var[feature] and song_features[feature] <= avg[feature]+var[feature]:
        arr.append(feature)

    feature = 'instrumentalness'
    if song_features[feature] >= avg[feature]-var[feature] and song_features[feature] <= avg[feature]+var[feature]:
        arr.append(feature)

    feature = 'liveness'
    if song_features[feature] >= avg[feature]-var[feature] and song_features[feature] <= avg[feature]+var[feature]:
        arr.append(feature)

    feature = 'valence'
    if song_features[feature] >= avg[feature]-var[feature] and song_features[feature] <= avg[feature]+var[feature]:
        arr.append(feature)
    return arr,len(arr)

def main():
    #Populate dataframe with list of playlists from excel
    playlists = excel_list_to_df()

    #Initialize array for final playlist outputted to user
    output_playlist = []

    #Take in user playlist,get info pertaining to average and variance
    user_playlist = get_user_playlist()
    user_avg,user_var = get_user_statistics()

    #Put all this info into an array
    for playlist in playlists:
        #This tells us how many features of the compared song are in range of the user playlist averages
        song_features = convert_playlist_to_dataframe(playlist)
        for song in song_features.iloc():
            if compare_features(user_avg,user_var,song)> 1 and song not in output_playlist:
                output_playlist.append(song['link'])



#CURRENT ISSUES
#REMOVE DUPLICATES
#What to do when only one song is inputted
#What to do if inputs are improper for user playlist, or if inputs song instead of playlist
#One of the spotipy functions maxes out at 100 songs
#Do we want to add a feature where you can also input a playlist you want to compare to your playlist
#Do a version where it compares an inputted song rather than inputted playlist

if __name__ == "__main__":
    main()