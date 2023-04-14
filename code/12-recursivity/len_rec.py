###############################################################################
## Ce programme calcule la longueur d'une chaine de caractères récursivement.
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-04-13
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################


def len_rec(val, count=0):
    if len(val) == 0:
        return count
    else:
        return len_rec(val[1:], count + 1)


# Alternative sans accumulateur
def len_rec2(val):
    if len(val) == 0:
        return 0
    else:
        return 1 + len_rec2(val[1:])


def test():
    def len_rec_test():
        assert len_rec("") == 0
        assert len_rec("abc") == 3
        assert len_rec("un autre test") == 13
    
    def len_rec2_test():
        assert len_rec2("") == 0
        assert len_rec2("abc") == 3
        assert len_rec2("un autre test") == 13

    len_rec_test()
    len_rec2_test()

test() # Enlever en commentaire pour exécuter les tests