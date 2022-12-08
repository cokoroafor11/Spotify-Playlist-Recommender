import tkinter as tk
from main import *
window = tk.Tk()
title = tk.Label(text = "Welcome to the Spotify Recommender!")



#Create Entry 
label = tk.Label(text="Link to Playlist")
entry = tk.Entry()
link = entry.get()

#Create button
run_app = tk.Button(window, text = "Run", command = lambda:run(link))
#Set locations for stuff
title.pack()
label.pack()
entry.pack()
run_app.pack()
window.mainloop()

#Export as excel
#Create new playlist in Spotify
#Print Excel
