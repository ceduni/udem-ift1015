###############################################################################
## Ce programme permet de faire la transposé d'une matrice
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-03-14
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################


def transpose(matrice):
    matrice_trans = [None] * len(matrice[0])
    for i in range(len(matrice_trans)):
        matrice_trans[i] = []
        for j in range(len(matrice)):
            matrice_trans[i].append(matrice[j][i])
            
    return matrice_trans    
    

# Exemple d'utilisation

grille = [[1,2,3], [4,5,6], [7,8,9]]
grille_trans = transpose(grille)
print("Matrice: " + str(grille))
print("Transposé: " + str(grille_trans))




#################################################################################
# Tests unitaires
#################################################################################

def test():
    def eq_matrice(m1,m2):
        if len(m1) != len(m2):
            return False
        for i in range(len(m1)):
            if len(m1[i]) != len(m2[i]):
                return False
            for j in range(len(m1[i])):
                if m1[i][j] != m2[i][j]:
                    return False
        return True
    
    assert eq_matrice(transpose([[1,2], [3,4], [5,6]]), [[1,3,5], [2,4,6]])
    assert eq_matrice(transpose([[1,2,3], [4,5,6], [7,8,9]]), [[1,4,7], [2,5,8], [3,6,9]])
    assert eq_matrice(transpose([[1,2,3,4], [5,6,7,8], [9,10,11,12]]), [[1,5,9], [2,6,10], [3,7,11], [4,8,12]])

# test() # Exécuter les tests