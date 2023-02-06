###############################################################################
## Ce programme démontre l'énoncé conditionnel if en Python.
## Il utilise le if pour afficher le reste d'une division si présent.
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-01-29
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

# Variables globales

a = 18
b = 7

print("Quotient: ", a // b)

if a % b != 0:
    print("Reste: ", a % b)