###############################################################################
## Ce programme calcule l'accélération et inclut deux cas de tests démontrant
## l'usage de la fonction de calcul.
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-02-01
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

# Fonction secondaire réalisant l'affichage de l'accélération

def display(acc, unit="m/s²"):
    """Cette fonction affiche la valeur de l'accélération avec une unité

    Args:
        acc (float): Valeur de l'accélération
        unit (str, optional): Valeur de l'unité. Defaults to "m/s²".
    """
    acc_absolu = abs(round(acc, 2))
    if (acc > 0):
        print("Accélération de:", acc_absolu, unit)
    elif (acc < 0):
        print("Décélération de:", acc_absolu, unit)
    else:
        print("Aucune accélération")


# Fonction principale réalisant le calcul de l'accélération

def acceleration(vi, vf, ti, tf):
    """Cette fonction calcule l'accélération et retourne sa valeur

    Args:
        vi (float): Vitesse initiale
        vf (float): Vitesse finale
        ti (float): Temps initial
        tf (float): Temps final

    Returns:
        float: Valeur de l'accélération
    """
    return (vf - vi) / (tf - ti)


# Fonction simulant deux cas de test

def test():
    test1 = acceleration(24.7, 36.1, 0, 2.47)
    test2 = acceleration(12.4, 0, 0, 2.55)
    display(test1)
    display(test2)


test() # Exécution des deux cas de test