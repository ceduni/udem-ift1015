###############################################################################
## Ce programme simule un tir pile-ou-face jusqu'à obtenir 5000 tirs pile
## Il démontre l'usage de la boucle while
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-02-03
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

# Imports

from random import random

# Variables globales

pile = 0
face = 0

# Boucle itérant sur le tir pile-ou-face

while pile < 5000:
    if random() < 0.5:
        pile += 1
    else: 
        face += 1 
tirs = pile + face

# Affichage du nombre de tirs effectués pour obtenir 5000 tirs pile

print("Cela a pris", tirs , "tirs pour donner", pile , "fois pile")
