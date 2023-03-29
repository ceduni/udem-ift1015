###############################################################################
## Ce programme permet de jouer au jeu de mots Boggle (en français) à 2.
## Dans cette version les mots ne peuvent être formés que de lettre sur une 
## même ligne, même colonne ou une même diagonale.
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-03-08
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################


import random

des_16 = [
    ("E", "T", "U", "K", "N", "O"),
    ("E", "V", "G", "T", "I", "N"),
    ("D", "E", "C", "A", "M", "P"),
    ("I", "E", "L", "R", "U", "W"),
    ("E", "H", "I", "F", "S", "E"),
    ("R", "E", "C", "A", "L", "S"),
    ("E", "N", "T", "D", "O", "S"),
    ("O", "F", "X", "R", "I", "A"),
    ("N", "A", "V", "E", "D", "Z"),
    ("E", "I", "O", "A", "T", "A"),
    ("G", "L", "E", "N", "Y", "U"),
    ("B", "M", "A", "Q", "J", "O"),
    ("T", "L", "I", "B", "R", "A"),
    ("S", "P", "U", "L", "T", "E"),
    ("A", "I", "M", "S", "O", "R"),
    ("E", "N", "H", "R", "I", "S"),
]

des_25 = [
    ("E", "T", "U", "K", "N", "O"),
    ("E", "V", "G", "T", "I", "N"),
    ("D", "E", "C", "A", "M", "P"),
    ("I", "E", "L", "R", "U", "W"),
    ("E", "H", "I", "F", "S", "E"),
    ("R", "E", "C", "A", "L", "S"),
    ("E", "N", "T", "D", "O", "S"),
    ("O", "F", "X", "R", "I", "A"),
    ("N", "A", "V", "E", "D", "Z"),
    ("E", "I", "O", "A", "T", "A"),
    ("G", "L", "E", "N", "Y", "U"),
    ("B", "M", "A", "Q", "J", "O"),
    ("T", "L", "I", "B", "R", "A"),
    ("S", "P", "U", "L", "T", "E"),
    ("A", "I", "M", "S", "O", "R"),
    ("E", "N", "H", "R", "I", "S"),
    ("A", "T", "S", "I", "O", "U"),
    ("W", "I", "R", "E", "B", "C"),
    ("Q", "D", "A", "H", "A", "U"),
    ("A", "C", "F", "L", "N", "E"),
    ("P", "R", "S", "T", "U", "G"),
    ("J", "P", "R", "X", "E", "Z"),
    ("E", "K", "V", "Y", "B", "E"),
    ("A", "L", "C", "H", "E", "M"),
    ("E", "D", "U", "F", "H", "K"),
]

TAILLE_MOT_MIN = 3
NB_TOUR_MAX = 3

def creer_joueur(nom):
    """Cette fonction crée un objet joueur

    Args:
        nom (str): Nom du joueur

    Returns:
        objet: Joueur: nom(str), mots(Mot[]), tour(int), termine(bool)
    """
    return {
        "nom": nom,
        "mots": [],
        "tour": 0,
        "termine": False
    }

def transpose(matrice):
    """Cette fonction retourne la transposée d'une matrice (tableau 2D)

    Args:
        matrice ([][]): Matrice à transposer

    Returns:
        [][]: Transposée de la matrice
    """
    matrice_trans = [None] * len(matrice[0])
    for i in range(len(matrice_trans)):
        matrice_trans[i] = []
        for j in range(len(matrice)):
            matrice_trans[i].append(matrice[j][i])
            
    return matrice_trans    

def diagonale(matrice):
    """Cette fonction retourne la liste des diagonales d'une matrice (tableau 2D)

    Args:
        matrice ([][]): Matrice

    Returns:
        [][]: Liste des diagonales de la matrice
    """

    nb_row = len(matrice)
    nb_col = len(matrice[0])
    result = []

    # Paroucrs des diagonales de gauche à droite
    for x in range(1, nb_row + nb_col):
        diago_valeurs = []
        if x % 2 == 0:
            i = x // 2
            j = 0
        else:
            i = 0
            j = x // 2
            
        if i == 0 and j == nb_col - 1 or i == nb_row - 1 and j == 0:
            continue

        while i < nb_row and j < nb_col:
            diago_valeurs.append(matrice[i][j])
            i += 1
            j +=1

        result.append(diago_valeurs)

    # Paroucrs des diagonales de droite à gauche
    for x in range(nb_row + nb_col - 1, 0, -1):
        diago_valeurs = []
        if x % 2 == 0:
            i = x // 2
            j = nb_col - 1
        else:
            i = 0
            j = x // 2

        if i == 0 and j == 0 or i == nb_row - 1 and j == nb_col - 1:
            continue

        while i < nb_row and j >= 0:
            diago_valeurs.append(matrice[i][j])
            i += 1
            j -=1

        result.append(diago_valeurs)

    return result

def est_valide(mot_cherche, grille):
    """Cette fonction vérifie si un mot valide: lettres adjacentes du mot sont adjacentes 
    dans le même ordre sur une colonne ou ligne de la grille

    Args:
        mot_cherche (str): Mot à valider
        grille ([][]): Grille

    Returns:
        bool: Valeur indiquant si le mot est valide
    """
    if len(mot_cherche) < TAILLE_MOT_MIN:
        return False

    mots = []

    def add_mot(matrice):
        for i in range(len(matrice)):
            if len(matrice[i]) >= TAILLE_MOT_MIN:
                mot = "".join(matrice[i])
                mots.append(mot)
                mots.append(mot[::-1])        
    
    add_mot(grille)
    grille_transpose = transpose(grille)
    add_mot(grille_transpose)
    diagonales = diagonale(grille)
    add_mot(diagonales)

    for mot in mots:
        if mot_cherche in mot:
            return True
        
    return False

def calcul_point(mot, grille):
    """Cette fonction calcule le nombre de points associé à un mot

    Args:
        mot (str): Mot
        grille ([][]): Grille

    Returns:
        int: Nombre de points
    """
    if len(mot) < 3:
        return 0

    if len(grille) == 4:
        match len(mot):
            case 3: return 1
            case 4: return 2
            case 5: return 3
            case 6: return 5
            case 7: return 8
            case _: return 10

    if len(grille) == 5:
        match len(mot):
            case 3: return 1
            case 4: return 2
            case 5: return 3
            case 6: return 4
            case 7: return 6
            case _: return 10

def ajout_mot(joueur, mot, grille):
    """Cette fonction ajoute un mot (structure) à la liste des mots d'un joueur

    Args:
        joueur (*): Objet joueur
        mot (str): Mot
        grille ([][]): Grille

    Returns:
        *: Objet mot
    """
    mot_formate = format_word(mot)
    valid = est_valide(mot_formate, grille)

    mot_struct = {
        "valeur": mot_formate,
        "valide": valid,
        "rejete": False,
        "point": 0 if not valid else calcul_point(mot_formate, grille),
    }

    joueur["mots"].append(mot_struct)

    return mot_struct

def generer_grille(taille):
    """Cette fonction génère une grille

    Args:
        taille (int): Taille de la grille (4, 5)

    Returns:
        [][]: Grille
    """
    if taille == 4:
        des = des_16
    elif taille == 5:
        des = des_25
    else:
        return []

    index_des = [i for i in range(taille**2)]
    random.shuffle(index_des)
    grille = [None] * taille

    for i in range(taille):
        grille[i] = [None] * taille
        for j in range(taille):
            index = index_des[i * taille + j]
            face = int(random.random() * 6)
            grille[i][j] = des[index][face]

    return grille

def afficher_grille(grille):
    print("-" + "----" * len(grille))
    for i in range(len(grille)):
        print("|", end="")
        for j in range(len(grille[i])):
            print(" " + grille[i][j] + " |", end="")
        print()
        print("-" + "----" * len(grille))


# Fonction faisant la somme des nombres valides.
def total(mots):
    """Cette fonction calcule le total des points d'une liste de mots 

    Args:
        mots ([]): Liste de mots (objet)

    Returns:
        int: Total des points
    """
    result = 0
    for mot in mots:
        if mot["valide"] and not mot["rejete"]:
            result += int(mot["point"])

    return result

def afficher_resultat(joueurs):
    """Cette fonction affiche le résultat des joueurs

    Args:
        joueurs ([]): Liste de joueurs
    """
    total_joueurs = []

    for joueur in joueurs:
        print(joueur["nom"].upper())
        print("-----------------------------")
        for mot in joueur["mots"]:
            if mot['rejete']:
                print(f"- {mot['valeur'].ljust(10)}   (x) -- REJETE")
            elif mot['valide']:
                print(f"- {mot['valeur'].ljust(10)}   ({mot['point']})")
            else:
                print(f"- {mot['valeur'].ljust(10)}   (x) -- ILLEGAL")
        print("=============================")
        total_joueur = total(joueur['mots'])
        total_joueurs.append(total_joueur)
        print(f"TOTAL: {total_joueur}\n")

    index_gagnant = total_joueurs.index(max(total_joueurs))
    print(f"{joueurs[index_gagnant]['nom']} a remporté la partie!")

def equiv(letter):
    """Cette fonction retourne la lettre équivalente sans accent

    Args:
        letter (string): Lettre à formater

    Returns:
        string: Lettre équivalente
    """
    letter_equiv = letter
    if letter.lower() in "éèêë": letter_equiv = "e"
    elif letter.lower() in "àâ": letter_equiv = "a" 
    elif letter.lower() in "ùû": letter_equiv = "u" 
    elif letter.lower() in "îï": letter_equiv = "i" 
    elif letter.lower() in "ô": letter_equiv = "o" 
    elif letter.lower() in "ç": letter_equiv = "c" 

    return letter_equiv if letter.islower() else letter_equiv.upper()    

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

    return result.upper()

def jouer(nb_joueur=2, taille = 4):
    jeu_termine = False

    def init():
        joueurs = []
        for i in range(nb_joueur):
            joueurs.append(creer_joueur(f"Joueur {i + 1}"))
        # for i in range(nb_joueur): joueurs.append(create_joueur(input(f"Nom joueur {i + 1}: ")))

        grille_accepte = False
        while not grille_accepte:
            grille = generer_grille(taille)
            afficher_grille(grille)
            grille_accepte = input("Jouer avec cette grille? [O] Oui [N] Non (nouvelle grille) ").upper() == "O"
        return joueurs, grille

    def partie_termine(joueurs):
        for joueur in joueurs:
            if not joueur["termine"] and joueur["tour"] < NB_TOUR_MAX:
                return False

        return True

    def get_joueur(tour, joueurs):
        index = tour % len(joueurs)

        if joueurs[index]["termine"]:
            return get_joueur(tour + 1, joueurs)

        return joueurs[index]
    
    def joueur_tour(joueur, grille):
        joueur["tour"] += 1
        print(f"> {joueur['nom']}")
        afficher_grille(grille)

        reponse = get_mot(joueur)
        if reponse is None:
            joueur["termine"] = True
        
        return reponse, joueur["termine"]

    def entree_valide(val):
        return val.isalpha() and len(val) >= 3

    def get_mot(joueur):
        re = ""
        while True:
            re = re if re in ["O", "N"] else input("As-tu un mot? [O] Oui [N] Non ").upper()
            if re not in ["O", "N"]:
                print("Veuillez taper [O] pour 'Oui' ou [N] pour 'Non'")
                continue
            if re == "N":
                return None

            mot = input(f"Mot {joueur['tour']}/{NB_TOUR_MAX}: ")
            if not entree_valide(mot):
                print("Écrivez un mot de 3 lettres ou plus.")
                continue

            return mot

    while not jeu_termine:
        joueurs, grille = init()

        tour = 0
        while not partie_termine(joueurs):
            joueur = get_joueur(tour, joueurs)
            mot, termine = joueur_tour(joueur, grille)
            if termine:
                tour += 1
                continue

            mot_struct = ajout_mot(joueur, mot, grille)
            if mot_struct["valide"]:
                mot_struct["rejete"] = input(f"Rejeter le mot '{mot_struct['valeur']}'? [O] Oui [N] Non ").upper() == "O"
            else:
                print("Mot n'est pas valide")

            tour += 1

        print("\nPARTIE TERMINÉE!\n")
        afficher_resultat(joueurs)

        jeu_termine = input("Rejouer une partie? [O] Oui [N] Non").upper() == "N"

jouer(2, 5) # Enlever en commentaire pour jouer une partie




#################################################################################
# Tests unitaires
#################################################################################


def test():
    grille_4 = [
        ["T", "I", "M", "E"],
        ["W", "O", "R", "D"],
        ["F", "A", "C", "T"],
        ["G", "A", "M", "E"],
    ]
    grille_5 = [
        ["P", "U", "Z", "Z", "L"],
        ["W", "O", "R", "D", "E"],
        ["B", "O", "G", "G", "L"],
        ["S", "E", "A", "R", "C"],
        ["F", "I", "N", "D", "H"],
    ]

    def rand_word(length):
        letters = "abcdefghijklmnopqrstuvwxyz"
        word = ""
        for _ in range(length): word += letters[random.randint(0, len(letters) - 1)]
        return word.upper()

    def rand_num(min, max, except_nums =[]):
        num = random.randint(min, max)
        while num in except_nums:
            num = random.randint(min, max)
        
        return num

    def generer_grille_test():
        print(f"> Test sur generer_grille()")
        try:
            for i in [4, 5]: 
                grille = generer_grille(i)
                assert len(grille) == i
                for ligne in grille:
                    assert len(ligne) == i
            print(f"    [PASS] Grille est générée lorsque la taille est valide")
        except AssertionError:
            print(f"    <FAIL> Grille est générée lorsque la taille est valide")

        try:
            for i in [4, 5]: 
                grille = generer_grille(i)
                for ligne in grille:
                    for lettre in ligne:
                        assert lettre.isalpha()
            print(f"    [PASS] Grille générée est composé de lettres")
        except AssertionError:
            print(f"    <FAIL> Grille générée est composé de lettres")
        
        try:
            for _ in range(100): 
                grille = generer_grille(rand_num(0, 1000, [3, 4]))
                assert len(grille) == 0
            print(f"    [PASS] Tableau vide générée lorsque la taille n'est pas valide")
        except AssertionError:
            print(f"    <FAIL> Tableau vide générée lorsque la taille n'est pas valide")
        
        try:
            for _ in range(100):
                grille1 = generer_grille(4)
                grille2 = generer_grille(4)
                assert grille1 != grille2
            print(f"    [PASS] Grille différente à chaque génération")
        except AssertionError:
            print(f"    <FAIL> Grille différente à chaque génération")
          
    def est_valide_test():
        print(f"> Test sur est_valide()")
        mots_valide_ligne = [grille_4[0][1:], grille_4[1][:], grille_4[2][1:], grille_4[3][:]]
        try:
            for i in range(len(mots_valide_ligne)):
                mot = "".join(mots_valide_ligne[i]) 
                assert est_valide(mot, grille_4) == True
            print(f"    [PASS] Mot est valide si formé de lettre adjacentes sur une même ligne")
        except AssertionError:
            print(f"    <FAIL> Mot est valide si formé de lettre adjacentes sur une même ligne")
            
        try:            
            for i in range(len(mots_valide_ligne)):
                mot = "".join(mots_valide_ligne[i])[::-1]
                assert est_valide(mot, grille_4) == True
            print(f"    [PASS] Mot est valide si formé de lettre adjacentes sur une même ligne (sens inverse)")
        except AssertionError:
            print(f"    <FAIL> Mot est valide si formé de lettre adjacentes sur une même ligne (sens inverse)")

        mots_valide_colonne = []
        for i in range(len(grille_4)):
            mot = [] 
            for j in range(len(grille_4)):
                mot.append(grille_4[j][i])
            mots_valide_colonne.append(mot)
        try:
            for i in range(len(mots_valide_colonne)):
                mot = "".join(mots_valide_colonne[i]) 
                assert est_valide(mot, grille_4) == True
            print(f"    [PASS] Mot est valide si formé de lettre adjacentes sur une même colonne")
        except AssertionError:
            print(f"    <FAIL> Mot est valide si formé de lettre adjacentes sur une même colonne")

        try:            
            for i in range(len(mots_valide_colonne)):
                mot = "".join(mots_valide_colonne[i])[::-1]
                assert est_valide(mot, grille_4) == True
            print(f"    [PASS] Mot est valide si formé de lettre adjacentes sur une même colonne (sens inverse)")
        except AssertionError:
            print(f"    <FAIL> Mot est valide si formé de lettre adjacentes sur une même colonne (sens inverse)")

        mots_valide_diagonale =  list(filter(lambda x: (len(x) >= TAILLE_MOT_MIN), diagonale(grille_4))) 
        try:
            for i in range(len(mots_valide_diagonale)):
                mot = "".join(mots_valide_diagonale[i]) 
                assert est_valide(mot, grille_4) == True
            print(f"    [PASS] Mot est valide si formé de lettres adjacentes sur une même diagonale")
        except AssertionError:
            print(f"    <FAIL> Mot est valide si formé de lettres adjacentes sur une même diagonale")

        try:            
            for i in range(len(mots_valide_diagonale)):
                mot = "".join(mots_valide_diagonale[i])[::-1]
                assert est_valide(mot, grille_4) == True
            print(f"    [PASS] Mot est valide si formé de lettres adjacentes sur une même diagonale (sens inverse)")
        except AssertionError:
            print(f"    <FAIL> Mot est valide si formé de lettres adjacentes sur une même diagonale (sens inverse)")
            print(f"> Test sur est_valide()")

        mots_non_valide = [grille_4[0][2:], grille_4[1][1:2], grille_4[2][:2]]
        try:
            for i in range(len(mots_non_valide)):
                mot = "".join(mots_non_valide[i]) 
                assert est_valide(mot, grille_4) == False
            print(f"    [PASS] Mot n'est pas valide si formé de moins de 3 lettres")
        except AssertionError:
            print(f"    <FAIL> Mot n'est pas valide si formé de moins de 3 lettres")
            
        try:
            for _ in range(100):
                mot = rand_word(4)
                assert est_valide(mot, grille_4) == False
            print(f"    [PASS] Mot n'est pas valide si formé de lettres qui ne sont pas sur la grille")
        except AssertionError:
            print(f"    <FAIL> Mot n'est pas valide si formé de lettres qui ne sont pas sur la grille")

        m1 = grille_4[0][1:]; m1.append(grille_4[0][0])
        m2 = grille_4[1][1:]; m2.append(grille_4[2][3])
        mots_non_valide = [m1, m2]    
        try:
            for i in range(len(mots_non_valide)):
                mot = "".join(mots_non_valide[i]) 
                assert est_valide(mot, grille_4) == False
            print(f"    [PASS] Mot n'est pas valide si formé de lettres qui ne sont pas adjacente")
        except AssertionError:
            print(f"    <FAIL> Mot n'est pas valide si formé de lettres qui ne sont pas adjacente")
    
    def calcul_point_test():    
        print(f"> Test sur calcul_point()")             

        points_4 = [0, 0, 0, 1, 2, 3, 5, 8, 10]
        for i in range(len(points_4)):
            point = points_4[i]
            try:
                assert calcul_point(rand_word(i), grille_4) == point
                print(f"    [PASS] Mot de {i} lettres retourne {point} points pour un grille 4x4")
            except AssertionError:
                print(f"    <FAIL> Mot de {i} lettres retourne {point} points pour un grille 4x4")
        try:
            point = 10
            for _ in range(8, 100):
                assert calcul_point(rand_word(i), grille_4) == point 
            print(f"    [PASS] Mot de plus de 8 lettres retourne {point} points pour un grille 4x4")
        except AssertionError:
            print(f"    <FAIL> Mot de plus de 8 lettres retourne {point} points pour un grille 4x4")

        points_5 = [0, 0, 0, 1, 2, 3, 4, 6, 10]
        for i in range(len(points_5)):
            point = points_5[i]
            try:
                assert calcul_point(rand_word(i), grille_5) == point
                print(f"    [PASS] Mot de {i} lettres retourne {point} points pour un grille 5x5")
            except AssertionError:
                print(f"    <FAIL> Mot de {i} lettres retourne {point} points pour un grille 5x5")
        
        try:
            point = 10
            for _ in range(8, 100):
                assert calcul_point(rand_word(i), grille_5) == point 
            print(f"    [PASS] Mot de plus de 8 lettres retourne {point} points pour un grille 5x5")
        except AssertionError:
            print(f"    <FAIL> Mot de plus de 8 lettres retourne {point} points pour un grille 5x5")
    
    generer_grille_test()
    est_valide_test()
    calcul_point_test()

# test() # Enlever en commentaire pour exécuter les tests
