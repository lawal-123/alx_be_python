FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    temperature = float(input("enter a temperature ? (celcius)"))
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    temperature = float(input("enter a temperature ? (fahrenheit)"))
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
temp_conv = float(input("enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
