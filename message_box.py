import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox

class MessageBox:
    def __init__(self,game):
        self.game = game


    def preparinggame(self):
        messagebox.showinfo('Ustawianie statkow', "Masz do wyboru:\n" 
                            "1 - czteromasztowiec\n"
                            "2 - trzymasztowce\n"
                            "3 - dwumasztowce\n"
                            "4 - jednomasztowce\n")

    def startgame(self):
       messagebox.showinfo('Gra', "Czas zacząć!\n"
                           "Klikaj na tablice przeciwnika\n"
                           ",aby zbic wszystkie statki\n")

    def win(self):
        messagebox.showinfo('Wygrana', "Gratulacje!\n"
                            "Wygrales z komputerem!")

    def lose(self):
        messagebox.showinfo('Przegrana', "Niestety, zostałeś pokonany\n"
                            "Zagraj ponownie! ;)")

