###############################################################################
## Ce programme permet de calculer le plus petit commun multiple (PPCM) entre
## deux nombres
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-02-02
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

# Fonction secondaire

def lire_nombre():
    """Cette fonction demande à l'utilisateur d'entrée un nombre

    Returns:
        int: Nombre entier fourni par l'utilisateur
    """
    return int(input("Entrer un nombre"))

def affiche(ppcm):
    """Cette fonction affiche la valeur d'un PPCM

    Args:
        ppcm (int): Plus petit commun multiple
    """
    print("Le plus petit commun multiple (PPCM) est:", ppcm)


# Fonction principale

def ppcm(num1, num2):
    """Calcule le plus petit commun multiple (PPCM) entre deux nombres

    Args:
        num1 (int): Nombre entier
        num2 (int): Nombre entier

    Returns:
        int: Valeur du PPCM
    """
    candidat = num1 if num1 > num2 else num2
    
    while True:
        if candidat % num1 == 0 and candidat % num2 == 0:
            return candidat
        candidat += 1




#################################################################################
# Tests
#################################################################################

num1 = lire_nombre()
num2 = lire_nombre()
ppcm_num1_num2 = ppcm(num1, num2)
affiche(ppcm_num1_num2)
