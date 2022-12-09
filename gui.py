import tkinter as tk
from tkinter import ttk
from main import *
from setup import *
from IPython.display import display

#Creating the Tkinter window and title
window = tk.Tk()
title = tk.Label(text = "Welcome to the Spotify Recommender!")



#Create Label for entry 
label = tk.Label(text="Link to Playlist")

#Create entry where user inputs link
entry = tk.Entry()
link = entry.get()

#Create button to run the function
run_button = tk.Button(window, text = "Get Songs!", command = lambda:run(link))


#Create button to get playlist statistics
statistics_button = tk.Button(window,text = "Get Stats", command = lambda:export_user_statistics(link))

#Set locations for various text and buttons
title.pack()
label.pack()
entry.pack()
run_button.pack(side="left")
statistics_button.pack(side="right")

#Mainloop makes sure the page stays open and keeps running
window.mainloop()


