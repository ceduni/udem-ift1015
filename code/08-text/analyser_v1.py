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
    for i in range(len(tab)):
        if tab[i] == val:
            return i

    return -1


def decouper(texte): 
    """Découpe un texte en tableau contenant uniquement des mots

    Args:
        texte (str): Texte à découper

    Returns:
        str[]: Tableau de mots
    """
    resultat = []
    debut = 0
    while debut < len(texte):
        if texte[debut].isalpha():
            i = debut+1
            while i < len(texte) and texte[i].isalpha():
                i += 1
            resultat.append(texte[debut:i])
            debut = i+1
        else:
            debut += 1
    return resultat


def frequence_mots(texte):
    """Retourne un tableau d'objet composé d'un mot et sa fréquence

    Args:
        texte (str): Texte 

    Returns:
        []: Tableau de fréquence de mots
    """
    vus = [] 
    resultat = [] 
    for mot in decouper(texte):
        pos = position(vus, mot)
        if pos >= 0:
            resultat[pos]["freq"] += 1
        else:
            vus.append(mot)
            resultat.append({"mot": mot, "freq": 1})
    return resultat


def imprimer_frequence(freq_mots):
    """Affiche la fréquence d'une liste de mots

    Args:
        freq_mots ([]): Tableau de fréquence de mots
    """
    for f in freq_mots:
        print("-", f["mot"] + ":", f["freq"])


def analyser(texte):
    imprimer_frequence(frequence_mots(texte))


analyser('il a un chat noir et un chat blanc')