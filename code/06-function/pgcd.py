###############################################################################
## Ce programme permet de calculer le plus grand commun diviseur (PGCD) entre
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

def affiche(pgcd):
    """Cette fonction affiche la valeur d'un PGCD

    Args:
        pgcd (int): Plus grand commun diviseur
    """
    print("Le plus grand commun diviseur (PGCD) est:", pgcd)


# Fonction principale

def pgcd(num1, num2):
    """Calcule le plus grand commun diviseur (PGCD) entre deux nombres

    Args:
        num1 (int): Nombre entier
        num2 (int): Nombre entier

    Returns:
        int: Valeur du PGCD
    """

    if num1 % num2 == 0:
        return num2
    
    candidat =  num1 if num1 < num2 else num2
    
    while True:
        if num1 % candidat   == 0 and num2 % candidat == 0:
            return candidat
        candidat -= 1




#################################################################################
# Tests
#################################################################################

num1 = lire_nombre()
num2 = lire_nombre()
pgcd_num1_num2 = pgcd(num1, num2)
affiche(pgcd_num1_num2)
