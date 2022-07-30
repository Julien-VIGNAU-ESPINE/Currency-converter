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

def choose_currency(window):
    # @brief  : Create the combobox to choose the currency to convert
    # @params : take the window in wich the combobox will be displayed
    # @return : return the currency code choosen
    
    currencies = ["USR", "EUR", "JPY", "GBP"]
    comboExample = ttk.Combobox(window, values = currencies)
    comboExample.pack()

def mainloop():
    window = create_window("Currency Converter")
    title = tk.Label(window, text="Currency Converter", font=("Arial", 25))
    title.pack()
    question = tk.Label(window, text="\n\nChoose currencies :", font=("Arial", 15))
    question.pack()
    choose_currency(window)
    to = tk.Label(window, text="To:", font=("Arial", 15))
    to.pack()
    choose_currency(window)
    window.mainloop()

mainloop()