import tkinter as tk
from tkinter import ttk
from main import *
import spotipy
window = tk.Tk()
title = tk.Label(text = "Welcome to the Spotify Recommender!")



#Create Entry 
label = tk.Label(text="Link to Playlist")
entry = tk.Entry()
link = entry.get()

#create progress bar
#pb = ttk.Progressbar(root,orient='horizontal',mode='indeterminate',length=280)

#Create button to run the function
run_button = tk.Button(window, text = "Get Songs!", command = lambda:run(link))


#Create button to get playlist statistics
statistics_button = tk.Button(window,text = "Get Stats", command = lambda:export_user_statistics(link))

#Set locations for stuff
title.pack()
label.pack()
entry.pack()
run_button.pack(side="left")
statistics_button.pack(side="right")
window.mainloop()

#Export as excel
#Create new playlist in Spotify
#Print Excel
