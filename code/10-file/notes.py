###############################################################################
## Ce programme calcul la moyenne d'un ensemble d'étudiants dont les notes sont
## stockées dans un fichier `notes.csv`. Le fichier est lu et les moyennes sont
## écrites dans un fichier `moyennes.csv`
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-03-23
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################


import os
from file_utils import *

PATH_COURANT = os.getcwd()
PATH_NOTES = os.path.join(PATH_COURANT, 'data/notes.csv')
PATH_MOYENNES = os.path.join(PATH_COURANT, 'data/moyennes.csv')

# Constantes
#------------------------------------------------------------------------------
COL_ID = "Identifiant"
COL_PRENOM = "Prenom"
COL_NOM = "Nom"
COL_DM1 = "DM1"
COL_DM2 = "DM2"
COL_DM3 = "DM3"
COL_INTRA = "Intra"
COL_FINAL = "Final"
COL_MOYENNE = "Moyenne"

COLONNES_NOTES = [COL_ID, COL_NOM, COL_PRENOM, COL_DM1, COL_DM2, COL_DM3, COL_INTRA, COL_FINAL]
COLONNES_MOYENNES = [COL_ID, COL_PRENOM, COL_NOM, COL_MOYENNE]

COEFFCIENT = {
    COL_DM1: 0.10,
    COL_DM2: 0.15,
    COL_DM3: 0.25,
    COL_INTRA: 0.2,
    COL_FINAL: 0.3
}

# Cette fonction calcule le total des notes d'un étudiant
def total_note(note):
    result = 0
    for key, value in COEFFCIENT.items():
        mark = float(note[key])
        result += mark * value
    note[COL_MOYENNE] = str(result)


# Cette fonction crée un objet note à partir d'un tableau de données
def create_obj_note(data):
    note = {}
    for i in range(len(COLONNES_NOTES)):
        note[COLONNES_NOTES[i]] = data[i]

    return note

# Cette fonction crée un objet moyenne à partir d'un objet note
def create_obj_moyenne(note):
    obj = {}
    for i in range(len(COLONNES_MOYENNES)):
        key = COLONNES_MOYENNES[i]
        obj[key] = note[key]

    return obj

# Cette fonction calcul la moyenne de chaque étudiant et retourne la liste des moyennes
def moyenne(matrice):
    resultat = []
    for rangee in matrice:
        note = create_obj_note(rangee)
        total_note(note)
        moyenne = create_obj_moyenne(note)
        resultat.append(moyenne)

    return resultat

# Cette fonction retourne le contenu d'un fichier CSV sous forme de tableaux 2D
def lire_csv(path):
    lignes = split_line(read_file(path))
    resultat = []
    for ligne in lignes:
        resultat.append(ligne.split(','))
    return resultat

# Cette fonction écrit le contenu d'un tableau 2D dans un fichier CSV
def ecrire_csv(path, records):
    content = ""
    for row in records:
        content += ",".join(row) + "\n"
    write_file(path, content)

# Fonction principale
def main(inpath, outpath):
    notes = lire_csv(inpath)
    moyennes = moyenne(notes)
    ecrire_csv(outpath, moyennes)

main(PATH_NOTES, PATH_MOYENNES)