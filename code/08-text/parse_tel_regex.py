###############################################################################
## Ce programme extrait et normalise (chiffres uniquement) les numéros de 
## téléphone présents dans un texte à l'aide d'expressions régulières.
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

import re

def trouve_nombre(phrase):
    phone_regex = re.compile(r'\d{3}[- ]?\d{3}[- ]?\d{4}|\d{3}[- ]?\d{4}')
    
    resultat = phone_regex.findall(phrase)

    return resultat

def format_nombre(telephones):
    sub_regex = re.compile(r'[- ]')

    for i in range(len(telephones)):
        tel = telephones[i]
        telephones[i] = sub_regex.sub("", tel)

    return telephones


phrases = [
    "Mon numéro est le 5142019988",
    "Tu peux me joindre au 701-3300 ou au 201-0228391",
    "Appelle-le (438 601 9911) demain au plus tard.",
    "Marc habite dans le 514. Tu peux l'appeler sur son cell (201-9988) ou au 514-201-9988. Si tu ne le trouves pas, appelle Tara (438 222 2015)"
]

for phrase in phrases:
    print(f"Numero trouvé dans la phrase: « {phrase} »")
    print(format_nombre(trouve_nombre(phrase)))
