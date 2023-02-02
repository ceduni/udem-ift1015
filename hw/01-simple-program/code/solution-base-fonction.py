###############################################################################
## Ce programme simule le calcul de l'accélération pour deux cas et affiche 
## la valeur du calcul. Il améliore la solution de base en introduisant une 
## fonction pour l'affichage.
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-02-01
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

# Constantes

unit = "m/s²"

# Fonction interne réalisant l'affichage de l'accélération

def display(acc):
    """Cette fonction affiche la valeur de l'accélération

    Args:
        acc (float): Valeur de l'accélération
    """
    acc_absolu =  abs(acc)
    if (acc > 0):
        print("Accélération de:", acc_absolu, unit)
    elif (acc < 0):
        print("Décélération de:", acc_absolu, unit)
    else:
        print("Aucune accélération")


# Cas de test 1: Cacul et affichage de l'accélaration 

vi_1, vf_1, ti_1, tf_1 = 24.7, 36.1, 0, 2.47    # Variables de calcul (vi, vf, ti, tf)
acc_1 = round((vf_1 - vi_1) / (tf_1 - ti_1), 2) # Calcul de l'accélération
display(acc_1)                                  # Affichage de l'accélération

# Cas de test 2: Cacul et affichage de l'accélaration 

vi_2, vf_2, ti_2, tf_2 = 12.4, 0, 0, 2.55       # Variables de calcul (vi, vf, ti, tf)
acc_2 = round((vf_2 - vi_2) / (tf_2 - ti_2), 2) # Calcul de l'accélération
display(acc_2)                                  # Affichage de l'accélération
