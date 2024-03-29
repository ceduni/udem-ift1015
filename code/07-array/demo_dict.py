###############################################################################
## Ce programme démontre l'usage de dictionnaire pour créer une structure
## énumérant diverses propriétés sur des valeurs entrées par un utilisateur.
## Une liste est utilisée pour accumuler les entrées structurées
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-03-22
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################


# Liste utilisée pour accumuler les entrées
Nombres = []

# Fonction de calcul
#------------------------------------------------------------------------------

# Fonction vérifiant qu’une valeur est valide
def est_valide(val):
    return val.isdigit()

# Fonction vérifiant si le nombre est pair
def est_pair(nb):
    est_pair = nb % 2 == 0

    return est_pair

# Fonction vérifiant si le nombre est premier
def est_premier(nb):
    if nb == 1:
        return True

    for i in range(2, nb):
        if (nb % i) == 0:
            return False

    return True

# Fonction faisant la somme des nombres valides.
def total():
    result = 0
    for nombre in Nombres:
        if nombre["valide"]:
            result += int(nombre["valeur"])

    return result


# Fonction de construction
#------------------------------------------------------------------------------

# Fonction ajoutant une valeur à la liste des nombres.
# La valeur est validée et ajoutée sous forme d'enregistrement (dictionnaire).
def ajout_nombre(val):
    index = len(Nombres) + 1
    valid = est_valide(val)

    nombre = {
        "index": index,
        "valeur": val,
        "valide": valid,
        "pair": None if not valid else est_pair(int(val)),
        "premier": None if not valid else est_premier(int(val)),
    }

    Nombres.append(nombre)


# Fonction principale du programme. 
# Le nombre d'itérations peut être passé en paramètre.
def main(compteur=5):
    for i in range(compteur):
        nb = input(f"Nombre {i+1}/{compteur}: ")
        ajout_nombre(nb)

    print("\nRAPPORT")
    for nombre in Nombres:
        if not nombre['valide']:
            print(f"{nombre['index']}) '{nombre['valeur']}' n'est pas un nombre")
        elif nombre['pair']:
            print(f"{nombre['index']}) '{nombre['valeur']}' est un nombre pair")
        else:
            print(f"{nombre['index']}) '{nombre['valeur']}' est un nombre impair")

    print(f"TOTAL: {total()}")


main() # Exécuter le programme