###############################################################################
## Ce programme calcule récursivement la fréquence d'un nombre dans un tableau
## de plusieurs niveaux
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-04-10
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

def freq_recursive(tab, nombre_cherche):
    if len(tab) == 0:
        return 0

    nombre = tab.pop()
    if (type(nombre) is list):
        freq = freq_recursive(nombre, nombre_cherche)
    else:
        freq = 1 if nombre == nombre_cherche else 0

    return freq + freq_recursive(tab, nombre_cherche)


print(freq_recursive([1, 2, [[3, 4, 1], 1, 2], 1], 4))
