FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    temperature = float(input("enter the temperature to convert? (celcius)"))
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    temperature = float(input("enter the temperature to convert? (fahrenheit)"))
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
