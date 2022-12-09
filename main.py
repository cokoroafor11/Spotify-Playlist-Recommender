from setup import *
import pandas as pd
import numpy as np
from IPython.display import display
from playlist_db_setup import *


def feature_list_to_df():
    df = pd.read_excel("spotify_features.xlsx")
    return df

def callback(text):
    try:
        user_songs = extract_songs(text)
    except Exception as x:
        print("You did not enter a valid URL/URI. Please try again.")


def get_user_statistics(song_features):
    '''Get statistics for the inputted playlist'''

    averages = {}
    variances = {}
    stdevs = {}
    maxes = {}
    mins = {}

    avg_dancebility= np.mean(song_features['danceability'])
    var_danceability = np.var(song_features['danceability'])
    std_danceability = np.std(song_features['danceability'])
    min_danceability = np.min(song_features['danceability'])
    max_danceability = np.max(song_features['danceability'])

    avg_energy = np.mean(song_features['energy'])
    var_energy = np.var(song_features['energy'])
    std_energy = np.std(song_features['energy'])
    min_energy = np.min(song_features['energy'])
    max_energy = np.max(song_features['energy'])

    avg_speechiness = np.mean(song_features['speechiness'])
    var_speechiness = np.var(song_features['speechiness'])
    std_speechiness = np.std(song_features['speechiness'])
    min_speechiness = np.min(song_features['speechiness'])
    max_speechiness = np.max(song_features['speechiness'])

    avg_acousticness = np.mean(song_features['acousticness'])
    var_acousticness = np.var(song_features['acousticness'])
    std_acousticness = np.std(song_features['acousticness'])
    min_acousticness = np.min(song_features['acousticness'])
    max_acousticness = np.max(song_features['acousticness'])

    avg_instrumentalness = np.mean(song_features['instrumentalness'])
    var_instrumentalness = np.var(song_features['instrumentalness'])
    std_instrumentalness = np.std(song_features['instrumentalness'])
    min_instrumentalness = np.min(song_features['instrumentalness'])
    max_instrumentalness = np.max(song_features['instrumentalness'])

    avg_liveness = np.mean(song_features['liveness'])
    var_liveness = np.var(song_features['liveness'])
    std_liveness = np.std(song_features['liveness'])
    min_liveness = np.min(song_features['liveness'])
    max_liveness = np.max(song_features['liveness'])

    avg_liveness = np.mean(song_features['valence'])
    var_valence = np.var(song_features['valence'])
    std_valence = np.std(song_features['valence'])
    min_valence = np.min(song_features['valence'])
    max_valence = np.max(song_features['valence'])

    averages['danceability'] = avg_dancebility
    averages['energy'] = avg_energy
    averages['speechiness'] = avg_speechiness
    averages['acousticness'] = avg_acousticness
    averages['instrumentalness'] = avg_instrumentalness
    averages['liveness'] = avg_liveness
    averages['valence'] = avg_liveness

    variances['danceability'] = var_danceability
    variances['energy'] = var_energy
    variances['speechiness'] = var_speechiness
    variances['acousticness'] = var_acousticness
    variances['instrumentalness'] = var_instrumentalness
    variances['liveness'] = var_liveness
    variances['valence'] = var_valence

    stdevs['danceability'] = std_danceability
    stdevs['energy'] = std_energy
    stdevs['speechiness'] = std_speechiness
    stdevs['acousticness'] = std_acousticness
    stdevs['instrumentalness'] = std_instrumentalness
    stdevs['liveness'] = std_liveness
    stdevs['valence'] = std_valence

    mins['danceability'] = min_danceability
    mins['energy'] = min_energy
    mins['speechiness'] = min_speechiness
    mins['acousticness'] = min_acousticness
    mins['instrumentalness'] = min_instrumentalness
    mins['liveness'] = min_liveness
    mins['valence'] = min_valence

    maxes['danceability'] = max_danceability
    maxes['energy'] = max_energy
    maxes['speechiness'] = max_speechiness
    maxes['acousticness'] = max_acousticness
    maxes['instrumentalness'] = max_instrumentalness
    maxes['liveness'] = max_liveness
    maxes['valence'] = max_valence
    

    return averages,variances,stdevs,mins,maxes


def print_user_statistics(statistics):
    '''Print statistics for the inputted playlist'''

    avg = statistics[0]
    var = statistics[1]
    std = statistics[2]
    min = statistics[3]
    max = statistics[4]

    print(f'''
        Average Danceability: {avg['danceability']}
        Variance in Danceability: {var['danceability']}
        Standard Deviation in Danceability: {std['danceability']}
        Minimum Danceability: {min['danceability']}
        Maximum Danceability: {max['danceability']}
        ''')
    print(f'''
        Average Energy: {avg['energy']}
        Variance in Energy: {var['energy']}
        Standard Deviation in Energy: {std['energy']}
        Minimum Energy: {min['energy']}
        Maximum Energy: {max['energy']}
        ''')
    print(f'''
        Average Speechiness: {avg['speechiness']}
        Variance in Speechiness: {var['speechiness']}
        Standard Deviation in Speechiness: {std['speechiness']}
        Minimum Speechiness: {min['speechiness']}
        Maximum Speechiness: {max['speechiness']}
        ''')
    
    print(f'''
        Average Acousticness: {avg['acousticness']}
        Variance in Acousticness: {var['acousticness']}
        Standard Deviation in Acousticness: {std['acousticness']}
        Minimum Acousticness: {min['acousticness']}
        Maximum Acousticness: {max['acousticness']}
        ''')

    print(f'''
        Average Instrumentalness: {avg['instrumentalness']}
        Variance in Instrumentalness: {var['instrumentalness']}
        Standard Deviation in Instrumentalness: {std['instrumentalness']}
        Minimum Instrumentalness: {min['instrumentalness']}
        Maximum Instrumentalness: {max['instrumentalness']}
        ''')

    print(f'''
        Average Liveness: {avg['liveness']}
        Variance in Liveness: {var['liveness']}
        Standard Deviation in Liveness: {std['liveness']}
        Minimum Liveness: {min['liveness']}
        Maximum Liveness: {max['liveness']}
        ''')    
    
    print(f'''
        Average Valence: {avg['valence']}
        Variance in Valence: {var['valence']}
        Standard Deviation in Valence: {std['valence']}
        Minimum Valence: {min['valence']}
        Maximum Valence: {max['valence']}
        ''')

    print(f'''
        Ranges in all features using variance:
        Danceability: {avg['danceability'] - var['danceability']} - {avg['danceability'] + var['danceability']}
        Energy: {avg['energy'] - var['energy']} - {avg['energy'] + var['energy']}
        Speechiness: {avg['speechiness'] - var['speechiness']} - {avg['speechiness'] + var['speechiness']}
        Acousticness: {avg['acousticness'] - var['acousticness']} - {avg['acousticness'] + var['acousticness']}
        Instrumentalness: {avg['instrumentalness'] - var['instrumentalness']} - {avg['instrumentalness'] + var['instrumentalness']}
        Liveness: {avg['liveness'] - var['liveness']} - {avg['liveness'] + var['liveness']}
        Valence: {avg['liveness'] - var['valence']} - {avg['liveness'] + var['valence']}

        Ranges in all features using standard deviation:
        Danceability: {avg['danceability'] - std['danceability']} - {avg['danceability'] + std['danceability']}
        Energy: {avg['energy'] - std['energy']} - {avg['energy'] + std['energy']}
        Speechiness: {avg['speechiness'] - std['speechiness']} - {avg['speechiness'] + std['speechiness']}
        Acousticness: {avg['acousticness'] - std['acousticness']} - {avg['acousticness'] + std['acousticness']}
        Instrumentalness: {avg['instrumentalness'] - std['instrumentalness']} - {avg['instrumentalness'] + std['instrumentalness']}
        Liveness: {avg['liveness'] - std['liveness']} - {avg['liveness'] + std['liveness']}
        Valence: {avg['liveness'] - std['valence']} - {avg['liveness'] + std['valence']}
        ''')
        

def export_user_statistics(input_playlist):
    df = pd.DataFrame(get_user_statistics(convert_playlist_to_dataframe(input_playlist)))
    df.index = ['Average','Variance','Std Dev','Min', 'Max']
    df.to_excel("Statistics.xlsx")       


def compare_features(avg,var,song_features):
    '''
    For each feature, this function checks if a given song is in range of user playlist average+-variance.
    '''
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
    return len(arr),arr

def export_playlist(playlist):
    '''Export the playlist to an excel sheet in the location of the project'''
    track_info = []

    #For each song, append the track name, artist and link as an array to the track info array
    for song in playlist:
        track_info.append([get_track_name(song),','.join(get_track_artists(song)),song])

    #Convert to dataframe and export to excel in same location as project
    df = pd.DataFrame(track_info,columns = ['Track Name', 'Artists', 'Link'])
    df.to_excel("Songs.xlsx")


def run(user_playlist_input):
    '''This controls the main flow of the application, connecting to the Gui'''
    #Initialize array for final playlist outputted to user
    output_playlist = []

    #Convert user playlist link to a database
    user_playlist = convert_playlist_to_dataframe(user_playlist_input)

    #Take in user playlist, get info pertaining to average and variance
    user_avg,user_var,user_std,user_min,user_max = get_user_statistics(user_playlist)

    #Print user playlist statistics
    print("Below are the statistics surrounding your inputted playlist")
    print_user_statistics(get_user_statistics(user_playlist))
    
    song_features = feature_list_to_df()

    #This tells us how many features of the compared song are in range of the user playlist averages
    for song in song_features.iloc():
        if (compare_features(user_avg,user_var,song)[0]> 1) & (song['link'] not in output_playlist):
            output_playlist.append(song['link'])    
    
    export_playlist(output_playlist)
    
features = feature_list_to_df()
display(features)
#display(convert_playlist_to_dataframe('https://open.spotify.com/playlist/5PJUOcZUy72vVk3OW54nX8?si=cd77f41837b3443f'))
#print(excel_list_to_df())
#run('https://open.spotify.com/playlist/5PJUOcZUy72vVk3OW54nX8?si=dcec28efd128458e')

#CURRENT ISSUES
#REMOVE DUPLICATES
#What to do when only one song is inputted
#What to do if inputs are improper for user playlist, or if inputs song instead of playlist
#One of the spotipy functions maxes out at 100 songs

if __name__ == "__main__":
   #run('https://open.spotify.com/playlist/5PJUOcZUy72vVk3OW54nX8?si=dcec28efd128458e')
   run()