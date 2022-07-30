# CURRENCY CONVERTER
# window.py
# A Julien VIGNAU-ESPINE project
# Author : Julien VIGNAU-ESPINE
# 30/07/2022 19:00

# This file contains all the necessaries to create the window and everything
# linked with the window


# imports
import tkinter as tk
from tkinter import ttk

def create_window(window_name):
    # @brief  : Create a simple tkinter window
    # @params : Take the name of hte window
    # @return : return the created window

    window = tk.Tk()
    window.title(window_name)
    window.geometry('600x500+50+50')
    return (window)

def mainloop():
    window = create_window("Currency Converter")
    window.mainloop()

mainloop()