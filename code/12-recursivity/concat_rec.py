###############################################################################
## Ce programme fait la concaténation d'une liste de mots récursivement 
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-04-10
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

def concat(liste_mots, index, resultat):
    if index == len(liste_mots):
        return resultat
    
    resultat += liste_mots[index]
    return concat(liste_mots, index + 1, resultat)


print(concat(["fin", "de", "session"], 0, ""))
