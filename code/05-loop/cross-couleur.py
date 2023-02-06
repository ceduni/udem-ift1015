couleur_gauche = ["bleu", 'rouge', 'vert', 'jaune', 'magenta', 'marron']
couleur_droite = ['blanc', 'rouge', 'violet', 'gris', 'orange', 'rose']

for gauche in couleur_gauche:
    for droite in couleur_droite:
        if gauche ==droite:
            print("Trouvé!", gauche)
            break
          