###############################################################################
## Ce programme simule un lancé de dé à 6 faces.
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-02-02
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

# Imports

import math
from random import random

# Fonction principale

def lancer_de():
    """Retourne un entier de 1 à 6 avec une probabilité égale

    Returns:
        int: Valeur entre 1 et 6
    """
    return math.floor(6 * random()) + 1


def lancer_des(n):
    """Retourne la somme de plusieurs lancés de dés

    Args:
        n (int): Nombre de lancé de dé

    Returns:
        int: Somme des lancés de dés
    """
    somme = 0
    
    for _ in range(n):
        somme += lancer_de()

    return somme 

def lancer_2des():
    """Retourne la somme de 2 lancés de dés

    Returns:
        int: Somme des 2 lancés de dés
    """
    return lancer_des(2)

