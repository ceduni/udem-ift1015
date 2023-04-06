###############################################################################
## Ce programme permet de joueur à une version simplifiée du jeu touché-coulé.
## Les bateaux de chaque joueur sont positionnées aléatoirement sur la grille.
## Le module turtle est utilisé pour afficher l'état des grilles.
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-03-30
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

from turtle import *
from random import random
import math
import logging

DEBUG = True # Mettre à False pour ne pas afficher les informations de déboggage

if DEBUG: 
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

# Paramètres du jeu

NB_BATEAU = 5
NB_COLONNE = 6
NB_LIGNE = 6
TAILLE_CASE = 16
ESPACE_CASE = 4

# Fonctions de dessin de base

def arc(r, angle):
    longueur_arc = 2 * math.pi * r * angle / 360
    n = int(longueur_arc / 3) + 1
    longueur_etape = longueur_arc / n
    angle_etape = float(angle) / n
    for _ in range(n):
        fd(longueur_etape)
        lt(angle_etape)

def circle(r):
    arc(r, 360)    

def carre(cote):    
    for _ in range(4):
        fd(cote); lt(90)

# Fonctions de dessin de la grille

def dessiner_case_vide(cote):
    pensize(1); pencolor(0,0,0) # config de la taille et couleur du stylo
    carre(cote)

def dessiner_case_rate(cote):
    pensize(2); pencolor(0, 0.5, 0.5) # config de la taille et couleur du stylo
    
    hypotenuse = math.sqrt(cote**2 + cote **2)
    
    carre(cote)
    lt(45); fd(hypotenuse)                 # diagonale gauche-droite
    pu(); rt(135); fd(cote); rt(135); pd() # positionnement
    fd(hypotenuse)                         # diagonale droite-gauche
    pu(); lt(135); fd(cote); lt(90); pd(); # positionnement     

def dessiner_case_touche(cote):
    pensize(4); pencolor(0.8, 0.3, 0) # config de la taille et couleur du stylo
    
    rayon = cote//2
    pu(); fd(rayon - 1); pd()
    circle(rayon)
    pu(); fd(-(rayon - 1)); pd()  # positionnement
    
def index_2_coord(x, y):
    return chr(ord("A") + x) + str(6 - y)

def est_rate(joueur, x, y):
    coord = index_2_coord(x, y)
    return coord in joueur["visite"] and coord not in joueur["bateau"] 

def est_touche(joueur, x, y):
    coord = index_2_coord(x, y)
    return coord in joueur["visite"] and coord in joueur["bateau"]
 
def positionner(x, y):
    pu(); fd(x); lt(90); fd(y); rt(90); pd()

def grille(cols, lignes, taille, espace, joueur):
    for x in range(cols):
        for y in range(lignes):
            positionner(x * (taille + espace), y * (taille + espace))
            if est_rate(joueur, x, y):
                dessiner_case_rate(taille)
            elif est_touche(joueur, x, y):
                dessiner_case_touche(taille)
            else:
                dessiner_case_vide(taille)
            positionner(-x * (taille + espace), -y * (taille + espace))

def barre(taille, longueur):
    pensize(taille); pencolor(0, 0.4, 0.8)

    lt(90); fd(longueur); 
    pu(); fd(-longueur); rt(90);  pd(); 
            
# Fonction redessinant les éléments graphiques           
def rafraichir(joueurs):
    clear()

    pu(); goto(-150,-60); pd()
    grille(NB_COLONNE, NB_LIGNE, TAILLE_CASE, ESPACE_CASE, joueurs[0])

    pu(); goto(0,-110); pd()
    longueur = 50 + (TAILLE_CASE + ESPACE_CASE) * NB_LIGNE + 50
    barre(10, longueur)
    
    pu(); goto(40,-60); pensize(1); pd()
    grille(NB_COLONNE, NB_LIGNE, TAILLE_CASE, ESPACE_CASE, joueurs[1])

def generer_bateau():
    bateaux = []
    while len(bateaux) < NB_BATEAU:
        x = int(random() * NB_COLONNE)
        y = int(random() * NB_LIGNE)
        coord = index_2_coord(x, y)
        if coord not in bateaux:
            bateaux.append(coord)
    return bateaux

def creer_joueur(nom):
    list_bateau = generer_bateau()
    logging.info(f"{nom}:  {list_bateau}")

    return {
        "nom": nom,
        "bateau": list_bateau, 
        "visite": [],
        "touche": 0
    }

def lire_coord(joueur):
    def est_valide(coord):
        if len(coord) != 2:
            return False
        return coord[0] in "ABCDEF" and coord[1] in "123456"

    coord = input(joueur["nom"] + ": ").upper()
    while not est_valide(coord):
        coord = input(joueur["nom"] + ": ").upper()
    
    return coord

def maj_grille(joueur, coord):
    if coord in joueur["visite"]:
        print("Oups! Déjà visitée.")
        return
    
    if coord in joueur["bateau"]:
        joueur["touche"] += 1
        print("Touché!")
    else:
        print("Raté!")

    joueur["visite"].append(coord)

def termine(joueurs):
    for joueur in joueurs:
        if joueur["touche"] == len(joueur["bateau"]):
            return True
        
    return False

def jouer():
    joueurs = [creer_joueur("Joueur 1"), creer_joueur("Joueur 2")]
    tour = 1
    
    rafraichir(joueurs)
    while not termine(joueurs):
        i = (tour + 1) % 2
        joueur_actif = joueurs[i]
        joueur_adverse = joueurs[i - 1]
        
        coord = lire_coord(joueur_actif)
        maj_grille(joueur_adverse, coord)
        
        rafraichir(joueurs)
        
        tour += 1
        
    print(f"{joueur_actif.get('nom')} a gagné!")
    
speed(0)
delay(0)
jouer()