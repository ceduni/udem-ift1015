###############################################################################
## Ce programme calcule la somme d'une liste de nombres récursivement.
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-04-02
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

def somme(nombres, result):
    if len(nombres) == 0:
        return result
    # print(nombres, result) # Enlever en commentaire pour avoir une trace de l'évolution de nombres et result
    num = nombres.pop()
    return somme(nombres, result + num)

print(somme([1, 2, 3, 4], 0))


# Alternative sans accumulateur
def somme2(nombres):
    if len(nombres) == 0:
        return 0

    num = nombres.pop()
    return num + somme2(nombres)

print(somme2([1, 2, 3, 4]))