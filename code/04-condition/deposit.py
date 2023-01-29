###############################################################################
## Ce programme démontre l'énoncé conditionnel if en Python.
## Il utilise le if-else pour afficher un message en différente langue
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-01-29
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

# Variables globales

language = "french"
    
# Configuration des questions messages selon la langue choisie

if language == "french":
    question = "montant?"
    warning = "montant incorrect"
else:
    question = "amount?"
    warning = "incorrect amount"

deposit = float(input(question))

# Validation du montant entré

if deposit < 0:
    print(warning)