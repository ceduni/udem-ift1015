from turtle import *

def carre(cote):
    for _ in range(4):
        fd(cote); lt(90)

def positionner(x, y):
    pu(); fd(x); lt(90); fd(y); rt(90); pd()

def grille(cols, lignes, taille, espace):
    for x in range(cols):
        for y in range(lignes):
            positionner(x * (taille + espace), y * (taille + espace))
            carre(taille)
            positionner(-x * (taille + espace), -y * (taille + espace))

speed(50)
grille(5,5,20,5)