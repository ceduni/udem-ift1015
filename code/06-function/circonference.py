import math

def rayon_valide(rayon):
    return rayon < 0

def lire_rayon(msg = "Entrer le rayon du cercle:"):
    rayon = input(msg)
    
    while not rayon_valide(rayon):
         print("Mauvaise valeur de rayon.")
         rayon = input(msg)

    return rayon

def circonference_cercle(rayon):
    return 2 * math.pi * rayon

def affiche_circonference(circonference):
    print("La circonférence est:", circonference)

