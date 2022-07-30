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

def create_window(window_name):
    # @brief  : Create a simple tkinter window
    # @params : Take the name of hte window
    # @return : return the created window

    window = tk.Tk()
    window.title(window_name)
    window.geometry('600x500+50+50')
    return (window)

def print_result(window, result, cur):
    # @brief  : Print the result in a tkinter.Label
    # @params : window - the window in which display the result
    #           result - the result to be displayed
    #           cur    - the currency
    # @return : Do not return anything (0)

    result_sentence = str(result) + " " + cur

    text = tk.Label(window, text="\n\nResult :\n", font=("Arial", 15)).pack()
    printed_result = tk.Label(window, text = result_sentence, font=("Arial", 15)).pack()

def take_inputs(window):
    # @brief  : Create the comboboxs to choose the currency 
    # and the input and convert it
    # @params : take the window in wich the combobox will be displayed
    # @return : Do not return anything (0)
    
    def make_conversion():
        # @brief  : convert the currency and print the result
        # @params : Do not take any params
        # @return : Do not return anything (0)

        cur1 = currency1.get()
        cur2 = currency2.get()
        print_result(window, convert(cur1, cur2, atoi(amount.get())), cur2)
        return (0)
    
    amount =tk.StringVar(window)
    cur_code_list = ["EUR", "IDR", "BGN", "GBP", "DKK", "CAD", "JPY",
    "HUF", "RON", "MYR", "SEK", "SGD", "HKD", "AUD", "CHF", "KRW", "CNY",
    "TRY", "HRK", "NZD", "THB", "USD", "NOK", "RUB", "INR", "MXN", "CZK",
    "BRL", "PLN", "PHP", "ZAR"]

    # Combobox to choose the first currency
    currency1 = ttk.Combobox(window, values = cur_code_list)
    currency1.set("Pick an Option")
    currency1.pack(padx = 5, pady = 5)

    to = tk.Label(window, text="To :", font=("Arial", 15)).pack()

    # Combobox to choose the second currency
    currency2 = ttk.Combobox(window, values = cur_code_list)
    currency2.set("Pick an Option")
    currency2.pack(padx = 5, pady = 5)

    # Input of the amount to be converted
    amount_text = tk.Label(window, text="Amount :", font=("Arial", 15)).pack()
    amount_input = tk.Entry (window, textvariable = amount).pack()

    # Final validation button
    skip_line = tk.Label(window, text="\n", font=("Arial", 15)).pack()
    Button = tk.Button(window, text = "Submit", command = make_conversion)
    Button.pack(padx = 5, pady = 5)

    return (0)

def mainloop():
    # Creation of the window
    window = create_window("Currency Converter")

    # Make a title
    title = tk.Label(window, text="Currency Converter", font=("Arial", 25))
    title.pack()
    
    # idications
    sentence = tk.Label(window, text="\n\nChoose currencies :", font=("Arial", 15))
    sentence.pack()

    # Combobox, inputs and convertion
    take_inputs(window)

    # Run the window
    window.mainloop()

    return (0)

if __name__ == "__main__":
    mainloop()