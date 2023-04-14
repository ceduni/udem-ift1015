###############################################################################
## Ce programme extrait et normalise les numéros de téléphone présents dans un
## texte en conservant uniquement les chiffres. 
## Un numéro de téléphone est composé de 7 ou 10 chiffres et chaque bloc de 
## chiffres peut être séparé d'un espace ou d'un trait. 
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-04-13
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

phrase = "Marc habite dans le 514. Tu peux l'appeler sur son cell (201-9988) ou au 514-201-9988. Si tu ne le trouves pas, appelle Tara (438 222 2015)"
tel = []
compteur = ""
for i in range(len(phrase)):
    c = phrase[i]
    if c.isdigit():
        compteur += phrase[i]
    elif c in "- " and phrase[i-1].isdigit():
        continue
    else:
        if len(compteur) == 7 or len(compteur) == 10:
            tel.append(compteur)
        compteur = ""

if len(compteur) == 7 or len(compteur) == 10:
    tel.append(compteur)

print(tel)
