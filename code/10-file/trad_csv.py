###############################################################################
## Ce programme prend en entrée un fichier CSV (.csv) et produit une version
## du fichier sans accent (écrit dans un autre fichier).
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-03-25
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################


import os
from file_utils import *

PATH_COURANT = os.getcwd()
PATH_SRC = os.path.join(PATH_COURANT, 'data/noms.csv')
PATH_TRAD = os.path.join(PATH_COURANT, 'data/noms_trad.csv')


def equiv(letter):
    """Cette fonction retourne la lettre équivalente sans accent

    Args:
        letter (string): Lettre à formater

    Returns:
        string: Lettre équivalente
    """
    match letter.lower():
        case "é" | "è" | "ê" | "ë": return "e" if letter.islower() else "E"
        case "à" | "â": return "a" if letter.islower() else "A"
        case "ù" | "û": return "u" if letter.islower() else "U"
        case "î" | "ï": return "i" if letter.islower() else "I"
        case "ô": return "o" if letter.islower() else "O"
        case "ç": return "c" if letter.islower() else "C"
        case _: return letter

def format_word(word):
    """Cette fonction retourne un mot en majuscule et sans accent

    Args:
        word (string): Mot à formater

    Returns:
        string: Mot formaté
    """
    result = ""
    for c in word:
        result += equiv(c)

    return result

def trad(records):
    result = [None] * len(records)
    for i in range(len(records)):
        result[i] = [None] * len(records[i])
        for j in range(len(records[i])):
            result[i][j] = format_word(records[i][j])
    return result

def trad_inline(records):
    for row in records:
        for i in range(len(row)):
            row[i] = format_word(row[i])

def lire_csv(path):
    lignes = split_line(read_file(path))
    resultat = []
    for ligne in lignes:
        resultat.append(ligne.split(','))
    return resultat

def ecrire_csv(path, records):
    content = ""
    print(records)
    for row in records:
        print(row)
        content += ",".join(row) + "\n"
    write_file(path, content)

# Fonction principale
def main(inpath, outpath):
    content = lire_csv(inpath)
    content_trad = trad(content)
    ecrire_csv(outpath, content_trad)

main(PATH_SRC, PATH_TRAD)