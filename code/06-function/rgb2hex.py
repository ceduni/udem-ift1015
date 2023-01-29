###############################################################################
## Ce programme converti un code de couleur RGB en hexadécimal.
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-01-29
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

# Fonctions internes

def int_to_hex(value):
    """Converti un nombre entier entre 0 et 255 en notation hexadécimale

    Args:
        value (int): Nombre entier entre 0 et 255

    Returns:
        string: Valeur hexadécimale en string
    """

    if value < 0 or value > 255:
        return None

    ALPHA = '0123456789abcdef'

    upper = value // 16
    lower = value % 16

    return ALPHA[upper] + ALPHA[lower]

def format_hex(val):
    """Formatte une valeur hexadécimal

    Args:
        val (string): Valeur hexadécimal

    Returns:
        string: Valeur hexadécimal formatté
    """
    return '#' + val.upper()


# Fonction principal faisant la conversion d'une couleur en RGB à hexadécimale

def rgb_to_hex(red, green, blue):
    """Converti une couleur en notation RGB en notation hexadécimale

    Args:
        red (int): Valeur du code rouge
        green (int): Valeur du code vert
        blue (int): Valeur du code bleu

    Returns:
        string: Couleur en notation hexadécimale
    """

    hex_code = int_to_hex(red) + int_to_hex(green) + int_to_hex(blue)

    return format_hex(hex_code)




#################################################################################
# Tests
#################################################################################

print(rgb_to_hex(255, 255, 255))   # blanc (#FFFFFF)
print(rgb_to_hex(255, 0, 0))       # rouge (#FF0000)
print(rgb_to_hex(0, 255, 0))       # vert  (#00FF00)
print(rgb_to_hex(0, 0, 255))       # bleu  (#0000FF)
print(rgb_to_hex(0, 0, 0))         # noir  (#000000) 
