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
from convert import *
import string

def atoi(str):
    resultant = 0
    for i in range(len(str)):
        resultant = resultant * 10 + (ord(str[i]) - ord('0'))        #It is ASCII substraction 
    return resultant

def create_window(window_name):
    # @brief  : Create a simple tkinter window
    # @params : Take the name of hte window
    # @return : return the created window

    window = tk.Tk()
    window.title(window_name)
    window.geometry('600x500+50+50')
    return (window)

def choose_currency_and_amount(window):
    # @brief  : Create the comboboxs to choose the currency 
    # and the input and convert it
    # @params : take the window in wich the combobox will be displayed
    # @return : return the chosen currencies code
    
    def retrieve():
        print(convert(currency1.get(), currency2.get(), atoi(amount.get())))
    
    amount =tk.StringVar(window)
    cur_code_list = ["USD", "EUR", "GBP", "JPY"]
    currency1 = ttk.Combobox(window, values = cur_code_list)
    currency1.set("Pick an Option")
    currency1.pack(padx = 5, pady = 5)
    to = tk.Label(window, text="To:", font=("Arial", 15)).pack()
    currency2 = ttk.Combobox(window, values = cur_code_list)
    currency2.set("Pick an Option")
    currency2.pack(padx = 5, pady = 5)
    amount_input = tk.Entry (window, textvariable = amount).pack()
    Button = tk.Button(window, text = "Submit", command = retrieve)
    Button.pack(padx = 5, pady = 5)

def mainloop():
    window = create_window("Currency Converter")
    title = tk.Label(window, text="Currency Converter", font=("Arial", 25))
    title.pack()
    question = tk.Label(window, text="\n\nChoose currencies :", font=("Arial", 15))
    question.pack()
    choose_currency_and_amount(window)
    window.mainloop()

mainloop()