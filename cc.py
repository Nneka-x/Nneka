

from forex_python.converter import CurrencyRates
cr = CurrencyRates()

amount = int(input("enter the amount you want to convert: "))
from_currency = input("Enter the currency code that has to be converted: ").upper()
to_currency = input("Enter the currency code to convert: ").upper()
output = cr.convert(from_currency, to_currency, amount)
final =  round(output, 2)
print("The amount is:", final)



