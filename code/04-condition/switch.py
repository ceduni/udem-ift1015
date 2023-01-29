###############################################################################
## Ce programme démontre l'énoncé conditionnel switch (`match`) en Python.
## Il utilise le switch pour afficher différent message selon la valeur 
## possédée par une variable
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-01-29
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

# Variables globales

lettre = "A"

# Affichage du message conditionnel en utilisant l'énoncé switch (`match`)

match lettre:
    case "A":
        print("Excellent!")
    case "B":
        print("Très bien!")
    case "C" | "D":
        print("Continue!")
    case _:
        print("À la prochaine fois!")