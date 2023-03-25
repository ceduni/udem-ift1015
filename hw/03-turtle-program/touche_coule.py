###############################################################################
## {Description du programme}
###############################################################################
## Auteur: {auteur}
## Date: {date_dernier_changement}
## Email: {contact_email}
###############################################################################


# from turtle import * # Enlever en commentaire en dehors de Codeboot
# import math          # Enlever en commentaire en dehors de Codeboot

def arc(r, angle):
    """Cette fonction permet de tracer un arc de cercle

    Args:
        r (int): Rayon de l'arc
        angle (int): Angle de l'arc
    """
    longueur_arc = 2 * math.pi * r * angle / 360
    n = int(longueur_arc / 3) + 1
    longueur_etape = longueur_arc / n
    angle_etape = float(angle) / n
    for _ in range(n):
        fd(longueur_etape)
        lt(angle_etape)


def cercle(r):
    """Cette fonction permet de dessiner un cercle

    Args:
        r (int): Longueur du rayon
    """
    arc(r, 360)


def carre(cote):
    """ette fonction permet de dessiner un carré

    Args:
        cote (int): Longueur d'un coté
    """
    for _ in range(4):
        fd(cote); lt(90)


def positionner(x, y):
    """Cette fonction permet de positionner la tortue relativement à son emplacement actuel

    Args:
        x (int): Nombre de pas en x
        y (int): Nombre de pas en y
    """
    pu(); fd(x); lt(90); fd(y); rt(90); pd()


def grille(cols, lignes, taille, espace):
    """Cette fonction permet de tracer une grille.

    Args:
        cols (int): Nombre de colonnes
        lignes (int): Nombre de lignes
        taille (int): Taille d'une case
        espace (int): Taille de l'espace entre chaque case
    """
    for x in range(cols):
        for y in range(lignes):
            positionner(x * (taille + espace), y * (taille + espace))
            carre(taille)
            positionner(-x * (taille + espace), -y * (taille + espace))


# Fonction principale du programme

def jouer():
    pass