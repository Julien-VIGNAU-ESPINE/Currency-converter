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
    # @return : return the chosen currencies code
    
    def retrieve():
        print(currency1.get(), currency2.get())
    
    cur_code_list = ["USD", "EUR", "GBP", "JPY"]
    currency1 = ttk.Combobox(window, values = cur_code_list)
    currency1.set("Pick an Option")
    currency1.pack(padx = 5, pady = 5)
    to = tk.Label(window, text="To:", font=("Arial", 15)).pack()
    currency2 = ttk.Combobox(window, values = cur_code_list)
    currency2.set("Pick an Option")
    currency2.pack(padx = 5, pady = 5)

    Button = tk.Button(window, text = "Submit", command = retrieve)
    Button.pack(padx = 5, pady = 5)


def mainloop():
    window = create_window("Currency Converter")
    title = tk.Label(window, text="Currency Converter", font=("Arial", 25))
    title.pack()
    question = tk.Label(window, text="\n\nChoose currencies :", font=("Arial", 15))
    question.pack()
    choose_currency(window)
    window.mainloop()

mainloop()