###############################################################################
## Ce programme simule le jeu Devine-le-mot et démontre une boucle `while`
## Il utilise le if-else pour afficher un message en différente langue
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-01-29
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

# Variables globales

NB_ESSAI = 5

while True:
    fin = input("Jouer une nouvelle partie?")
    if fin == "n" or fin == "non":
        break

    compteur_essai = 0
    mot = ""

    while not(len(mot) >= 5 and len(mot) <= 10):
        mot = input("Entrer un mot (5-10 caractères)")

    print("Mot à deviner de", len(mot), "caractères")

    while compteur_essai < NB_ESSAI:
        print("Essai #", compteur_essai + 1)
        tentative = input("Mot ou lettre:")
    
        if tentative == mot:                          
            print("Mot trouvé!")
            break
        elif len(tentative) == 1 and tentative in mot: 
            print("Bonne lettre")
        else:
            print("Essaie encore")
            compteur_essai += 1
