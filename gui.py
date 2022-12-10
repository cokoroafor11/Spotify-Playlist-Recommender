'''
Chinedu Okoroafor and Ignacio Villasmil
'''

from tkinter import ttk
from main import *
from setup import *
from tkinter import *
from IPython.display import display
from functools import partial
import tkinter as tk

class Recommender(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('600x200')
        self.title = Label(text = "Welcome to the Spotify Recommender!")
        self.instructions1 = Label(text = "Instructions: Input link, then click the button to get your recommended songs.") 
        self.instructions2= Label(text ="If you're interested in your playlist statistics, click Get Stats.")
        self.entry = tk.Entry(self)
        self.button = tk.Button(self,text="Get Songs",command = [self.get_input,self.run_main])
        self.button.bind('<Button-1>',lambda run: self.run_main())
        self.button2 = tk.Button(self,text="Get Stats",command = [self.get_input,self.get_statistics])
        self.button2.bind('<Button-1>',lambda run: self.get_statistics())
        self.title.pack()
        self.entry.pack()
        self.button.pack()
        self.button2.pack()
        self.instructions1.pack()
        self.instructions2.pack()

    def get_input(self):
        print(self.entry.get())
        link = self.entry.get()
        return link

    def run_main(self):
       run(self.get_input())
    
    def get_statistics(self):
        export_user_statistics(self.get_input())

recommender = Recommender()

recommender.mainloop()

