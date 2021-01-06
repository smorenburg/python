#!/usr/bin/env python3

fahrenheit = float(
    input(
        'What temperature (in Farenheit) would you '
        'like to convert to Celsius? '
    )
)
celsius = (fahrenheit - 32) * 5 / 9

print(fahrenheit, 'F is', round(celsius, 2), 'C')
