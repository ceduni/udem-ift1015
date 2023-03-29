###############################################################################
## Ce programme décompose un texte en mots et affiche combien de fois apparait 
## chaque mot dans le texte.
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-03-22
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################


def position(tab, val): 
    """Retourne la position d'une valeur dans un tableau ou -1

    Args:
        tab ([]): Tableau dans lequel on cherche la valeur
        val (*): Valeur recherchée

    Returns:
        int: Position de la valeur dans le tableau
    """
    return ''.join(tab).find(val)


def decouper(texte):
    """Découpe un texte en tableau contenant uniquement des mots

    Args:
        texte (str): Texte à découper

    Returns:
        str[]: Tableau de mots
    """
    resultat = texte.split(" ")
    i = len(resultat) - 1
    while i > 0:
        if not resultat[i].isalpha():
            resultat[i].pop(i)
        i -= 1

    return resultat


def frequence_mots(texte):
    """Retourne un d'objet contenant tous les mots et leur fréquence

    Args:
        texte (str): Texte 

    Returns:
        *: Objet contenant les mots et leur fréquence
    """

    resultat = {}  
    for mot in decouper(texte):
        if mot in resultat.keys():
            resultat[mot] += 1
        else:
            resultat[mot] = 1

    return resultat

def imprimer(freq_mots):
    """Affiche la fréquence d'une liste de mots

    Args:
        freq_mots (*): Objet contenant les mots et leur fréquence
    """
    for fm in freq_mots.items():
        print(f'- {fm[0]}: {fm[1]}')


def analyser(texte):
    imprimer(frequence_mots(texte))


analyser('il a un chat noir et un chat blanc')
