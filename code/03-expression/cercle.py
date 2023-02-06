###############################################################################
## Ce programme démontre le calcul du périmètre et de l'aire d'un cercle
## Il utilise la libraire `math` pour récupérer la valeur du nombre PI
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-01-29
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

# Imports

import math

# Variables globales, constantes

r = 3

# Calcul de la circonférence (périmètre) et de l'aire

circonference = 2 * math.pi * r
aire = math.pi * r ** 2

# Affichage du résultat du calcul de la circonférence et de l'aire
# La fonction `format` est utilisé pour paramétrer le message affiché

print("Un cercle de {0} cm a une circonférence de {1} cm et une aire de {2} cm²".format(r, circonference, aire))
