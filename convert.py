# CURRENCY CONVERTER
# calcs.py
# A Julien VIGNAU-ESPINE project
# Author : Julien VIGNAU-ESPINE
# 30/07/2022 19:00

# This file contains all the necessaries to calculate and to convert currencies

#imports
from forex_python.converter import CurrencyRates


def convert(currency1, currency2, amount):
    # @brief  : Convert a currency into an other
    # @params : take currency code of the first currency, the currency code of
    #           the destination, and the amount to convert
    # @return : return the converted value

    cr = CurrencyRates()
    result = cr.convert(currency1, currency2, amount)
    return (result)