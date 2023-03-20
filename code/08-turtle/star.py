from turtle import *

def polygone_reg_etoile(cote, nb_sommet):
    angle = 180 / nb_sommet
    for _ in range(nb_sommet):
        fd(cote)
        lt(180 - angle)



def init():
    reset()
    pu()
    bk(80)
    pd()

init()
polygone_reg_etoile(160, 5)
init()
polygone_reg_etoile(160, 11)
init()
polygone_reg_etoile(160, 51)
