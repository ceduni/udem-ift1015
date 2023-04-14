###############################################################################
## Ce programme démontre l'usage d'expressions régulières pour récupérer les
## numéros de salle présent dans un texte.
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-03-15
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

import re

phrase = "Ce cours utilisera la salle 1140 et la salle 1360 du Pavillon André-Aisenstadt. Les salles N-515 du Pav. Roger-Gaudry et Z-110 du Pav. Claire-McNicoll seront utilisés pour les examens"

# Récupère toute suite de 4 nombres
salle_regex = re.compile(r'\d\d\d\d')
print(f'Salle: {salle_regex.findall(phrase)}')

# Récupère toute suite de 4 nombres ou toute suite d'un caractère 
# (alphanumérique ou underscrore) suivi d'un trait suivi de 4 nombres
salle_regex = re.compile(r'\d\d\d\d|\w-\d\d\d')
print(f'Salle: {salle_regex.findall(phrase)}')

# Récupère toute suite de nombres (1 ou plus)
salle_regex = re.compile(r'\d+')
print(f'Salle: {salle_regex.findall(phrase)}')

# Récupère toute suite d'un caractère (alphanumérique ou underscrore) suivi
# d'un trait suivi de nombres (1 ou plus)
salle_regex = re.compile(r'\w-\d+')
print(f'Salle: {salle_regex.findall(phrase)}')

# Récupère toute suite d'un caractère (alphanumérique ou underscrore) suivi
# d'un trait (optionnel) suivi de nombres (1 ou plus)
salle_regex = re.compile(r'\w-?\d+')
print(f'Salle: {salle_regex.findall(phrase)}')