###############################################################################
## Ce programme produit la représentation binaire d'un nombre décimal.
## La représentation binaire est construite récursivement.
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-04-02
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

def binaire(N):
    if N == 0:
        return ""
    return "" + binaire(N//2) + str(N % 2)


print(binaire(13))
