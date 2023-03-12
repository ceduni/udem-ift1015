###############################################################################
## Ce programme permet de trier un tableau en ordre croissant
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-03-03
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

def trier(tab):
    echange = True
    while echange:
        echange = False
        for i in range(len(tab) - 1):
            if tab[i] > tab[i + 1]:
                temp = tab[i]
                tab[i] = tab[i + 1]
                tab[i + 1] = temp
                echange = True


def test_trier():
    tab1 = [23, 71, 56, 42]
    tab1x = tab1.copy()
    trier(tab1)
    assert len(tab1) == len(tab1x)
    for i in tab1x:
        assert i in tab1
    for i in range(len(tab1) - 1):
        assert tab1[i] <= tab1[i + 1]

test_trier()