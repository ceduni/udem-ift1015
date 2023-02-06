###############################################################################
## Ce programme calcul le prix brut d'un produit.
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-01-30
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

TAUX_TPS = 0.05
TAUX_TVQ = 0.09975

def arrondi(prix):
    return round(prix * 100) / 100.0

def tps(prix):
    return arrondi(prix * TAUX_TPS)

def tvq(prix):
    return arrondi(prix * TAUX_TVQ)

def prix_brut(prix):
    return arrondi(prix + tps(prix) + tvq(prix))




#################################################################################
# Tests
#################################################################################

print(prix_brut(5))