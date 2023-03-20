from turtle import *


def polygone_reg(cote, nb_cote):
    for _ in range(nb_cote):
        fd(cote)
        lt(360 / nb_cote)


def carre(cote):
    polygone_reg(cote, 4)


def triangle(cote):
    polygone_reg(cote, 3)


def losange(cote):
    for _ in range(2):
        fd(cote)
        rt(120)
        fd(cote)
        rt(60)

def hexagone(cote):
    for _ in range(6):
        triangle(cote)
        rt(60)

def cube(cote):
    for _ in range(3):
        losange(cote)
        rt(120)


def pyramide(cote, n):
    pu()
    for couche in range(n, 0, -1):
        for _ in range(couche):
            pd()
            triangle(cote)
            pu()
            fd(cote)
        bk(cote*couche)
        rt(60)
        fd(cote)
        lt(60)
    pd()

def bague(cote):
    for i in range(12):
        if i % 2 == 0:
            triangle(cote)
        else:
            carre(cote)
        pu()
        fd(cote)
        pd()


# polygone_reg(50, 6)  # hexagone
# carre(50)           # carré
# polygone_reg(2, 60)  # cercle
# reset()
# triangle(80)
# reset()
# losange(80)
# reset()
# hexagone(80)
# reset()
# cube(80)
# reset()
# pyramide(16, 5)
# reset()
# bague(25)