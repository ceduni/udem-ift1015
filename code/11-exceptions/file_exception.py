###############################################################################
## Ce programme démontre l'usage de try..except pour traiter les exceptions
## pouvant survenir lors des opérations de manipulation de fichier
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-04-02
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

from datetime import date

try:
    path = input("Entrer un chemin: ")
    file = open(path) # Ici le fichier est ouvert en mode lecture (ajouter 'a' pour résoudre l'exception)
    try:
        file.write(f"\nDernière consultation: {date.today()}")
    except:
        print("Une erreur est survenue lors de la modification du fichier.")
    finally:
        file.close()
except:
    print("Une erreur est survenue lors de l’ouverture du fichier.")
