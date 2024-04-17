from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
import sys

def CCurrency(amount, convert_from, convert_to):
    c = CurrencyRates()
    if amount == 0:
        print("No one can change currency if you don't have one")
    else:
        converted_amount = c.convert(convert_from, convert_to, amount)
        print(converted_amount)
        return converted_amount

def knowyourcurrencybylogo(currency_name):
    c = CurrencyCodes()
    get_symbol = c.get_symbol(currency_name)
    return get_symbol

def knowyourcurrency_name(currencynames):
    c = CurrencyCodes()
    c.get_currency_name(currencynames)
    return c.get_currency_name(currencynames)


print("---Hello to the convertion centre")
print(" 1. Change your currency to another Currency")
print(" 2. Know your currency by logo")
print(" 3. Know your currency by name")
print(" 4. Exit")

choice = input("Enter your choice: ")
if choice == "1":
    amount = float(input("Enter the amount you would like to convert: "))
    convert_from = input("Enter the name of the currency you would like to convert From: ").upper()
    convert_to = input("Enter the name of the currency you would like to convert To: ").upper()
    CCurrency(amount, convert_from, convert_to)

if choice == "2":
    currency_name = input("Enter your currency to get logo if it!")
    knowyourcurrencybylogo(currency_name)

if choice == "3":
    currencyname = input("Enter the currency abbriviation to get name ")
    knowyourcurrency_name(currencyname)

if choice == "4":
    sys.exit()


