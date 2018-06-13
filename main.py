"""
projekt statki,
Ambrozy Pala II rok Informatyka
python 3,
gui - tkinter
"""

from tkinter import *
from PIL import ImageTk, Image
import random
import sys
import os
import tkinter
import time
import math
import select
from collections import Counter
import dialog as Dialog

from game_flow import GameFlow


class MainMenu(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.game = parent
        self.title("STATKI")
        self.resizable(width=tkinter.FALSE, height=tkinter.FALSE)
        self.windowWidth= parent.winfo_reqwidth()
        self.windowHeight = parent.winfo_reqwidth()
        self.positionRight = int(parent.winfo_screenwidth()/2 - self.windowWidth/2)
        self.positionDown = int(parent.winfo_screenheight()/2 - self.windowHeight/2)
        self.geometry('{}x{}+{}+{}'.format(400,410,self.positionRight, self.positionDown))
        #self.geometry('{}x{}+800+200'.format(400, 410))
        self.configure(background="#48c0b6")

        self.title_text = tkinter.Label(self, text="STATKI", bg="white", fg="black")
        self.title_text.config(font=("Helvetica", 28, "bold"))
        self.title_text.pack(pady=17, fill=X)

        self.startgame_button = tkinter.Button(self, text="Start Game", fg="green", height=3, width=26,
                                               command=lambda: self.on_startgame_click())
        self.startgame_button.pack(pady=10)

        self.endgame_button = tkinter.Button(self, text="End Game", fg="red", height=3, width=26,
                                             command=parent.destroy)
        self.endgame_button.pack(pady=10)

        self.footprint_text = tkinter.Label(self, text="Python Project in TKinter GUI")
        self.footprint_text.config(font=("Courier", 10), background="#48c0b6")
        self.footprint_text.pack(side=tkinter.BOTTOM)

        self.footprint_second_text = tkinter.Label(self, text="Created by Ambrozy Pala")
        self.footprint_second_text.config(font=("Courier", 10), background="#48c0b6")
        self.footprint_second_text.pack(side=tkinter.BOTTOM)

    def on_startgame_click(self):
        game_flow = GameFlow(self.game)
        game_flow.run()
        self.destroy()



def ConfigureGame():
    game = tkinter.Tk()
    game.withdraw()

    MainMenu(game)
    game.mainloop()


if __name__ == "__main__":
    ConfigureGame()
