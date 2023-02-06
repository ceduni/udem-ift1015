###############################################################################
## Ce programme converti une température en Celcius en Fahrenheit et en Kelvin
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-01-30
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################


def celcius_to_fahrenheit(temp_celcius):
    return temp_celcius * 9/5 + 32

def celcius_to_kelvin(temp_celcius):
    return temp_celcius + 273.5

def temp_conv(temp_celcius, type = 'F'):
    temp_fahrenheit = celcius_to_fahrenheit(temp_celcius)
    temp_kelvin = celcius_to_kelvin(temp_celcius)
    
    if type == 'F': 
        return temp_fahrenheit
    if type == 'K':
        return temp_kelvin
