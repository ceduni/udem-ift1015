###############################################################################
## Ce programme permet de jouer au jeu de mots Boggle (en français).
## Dans cette version, les mots peuvent être formés de toute lettre adjacente.
## La vérification d'un mot se fait par un parcours récursif de la grille.
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-03-08
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################


import random
import sys

# Classe d'exception personnalisée
class InvalidGridSizeException(Exception):
    "Soulever lorsque la taille de la grille est différent de 4 ou 5"
    pass


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


def est_valide(mot, grille):
    """Cette fonction vérifie si un mot valide

    Args:
        mot_cherche (str): Mot à valider
        grille ([][]): Grille

    Returns:
        bool: Valeur indiquant si le mot est valide
    """
    start_indexes = find_indexes(mot[0], grille)

    for index in start_indexes:
        if parcours_grille([], index, 0, mot, grille):
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


def find_indexes(lettre, grille):
    """Cette fonction trouve les indexes où se trouvent une lettre dans la grille

    Args:
        lettre (str): Lettre à trouver
        grille ([][]): Grille

    Returns:
        int[]: Liste des indexes
    """
    indexes = []
    taille = len(grille)
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == lettre:
                indexes.append(i * taille + j)
    return indexes


def get_lettre(index, grille):
    """Cette fonction récupère une lettre dans la grille à partir d'un index donné

    Args:
        index (int): Index de la lettre dans la grille
        grille ([][]): Grille

    Returns:
        str: Lettre trouvée
    """
    taille = len(grille)
    i = index // taille
    j = index % taille
    return grille[i][j]


def voisins(index, taille):
    """Cette fonction récupère la liste des voisins d'un index d'une grille

    Args:
        index (int): Index actuel
        taille (int): Taille de la grille (4, 5)

    Returns:
        int[]: Liste des indexes voisins
    """
    left = -1 if index % taille == 0 else index - 1
    right = -1 if (index + 1) % taille == 0 else index + 1
    up = -1 if index < taille else index - taille
    down = -1 if index > taille*(taille - 1) else index + taille

    diag_lu = -1 if left == -1 or up == -1 else index - taille - 1
    diag_ru = -1 if right == -1 or up == -1 else index - taille + 1
    diag_rd = -1 if right == -1 or down == -1 else index + taille + 1
    diag_ld = -1 if left == -1 or down == -1 else index + taille - 1

    neighbours = []
    index_max = taille ** 2 - 1
    for i in [left, right, up, down, diag_lu, diag_ru, diag_rd, diag_ld]:
        if i >= 0 and i <= index_max:
            neighbours.append(i)
    return neighbours


def parcours_grille(visite, grille_index, mot_index, mot, grille):
    """Cette fonction parcours récursivement la grille à partir d'un index de départ
    afin de trouver un chemin menant au mot complet

    Args:
        visite (int[]): Liste des indexes visitées
        grille_index (int): Indexe actuel dans la grille
        mot_index (int): Indexe actuel dans le mot
        mot (str): Mot recherché dans la grille
        grille ([][]): Grille

    Returns:
        bool: Valeur indiquant si un chemin décrivant le mot existe
    """

    if grille_index in visite:
        return False

    visite.append(grille_index)
    lettre = get_lettre(grille_index, grille)

    if lettre != mot[mot_index]:
        return False

    if mot_index == len(mot) - 1 and lettre == mot[-1]:
        return True

    neighbours = voisins(grille_index, len(grille))
    for n in neighbours:
        if parcours_grille(visite.copy(), n, mot_index + 1, mot, grille):
            return True
    return False


def generer_grille(taille):
    """Cette fonction génère une grille

    Args:
        taille (int): Taille de la grille (4, 5)

    Returns:
        [][]: Grille
    """
    if taille not in [4, 5]:
        raise InvalidGridSizeException("La taille reçue n'est pas supportée")
    
    if taille == 4:
        des = des_16
    elif taille == 5:
        des = des_25

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
    """Cette fonction affiche une grille dans la console

    Args:
        grille ([][]): Grille
    """
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
    match letter:
        case "é" | "è" | "ê" | "ë": return "e"
        case "à" | "â": return "a"
        case "ù" | "û": return "u"
        case "î" | "ï": return "i"
        case "ô": return "o"
        case "ç": return "c"
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

    return result.upper()


def jouer(nb_joueur=2, taille=4):
    print(sys.argv)
    # Récupération des arguments passés au programme
    if len(sys.argv) > 1:
        nb_joueur = sys.argv[1]
    if len(sys.argv) > 2:
        taille = sys.argv[2]
    
    jeu_termine = False

    # Cette fonction initialise les joueurs et de la grille
    def init():
        joueurs = []
        for i in range(nb_joueur):
            nom = input(f"Nom joueur {i + 1}: ")
            if len(nom) == 0: nom =f"Joueur {i + 1}"
            joueurs.append(creer_joueur(nom))

        grille_accepte = False
        while not grille_accepte:
            grille = generer_grille(taille)
            afficher_grille(grille)
            grille_accepte = input("Jouer avec cette grille? [O] Oui [N] Non (nouvelle grille) ").upper() == "O"
        return joueurs, grille

    # Cette fonction vérifie si la partie est terminée
    def partie_termine(joueurs):
        for joueur in joueurs:
            if not joueur["termine"] and joueur["tour"] < NB_TOUR_MAX:
                return False

        return True

    # Cette fonction récupère le joueur jouant le tour
    def get_joueur(tour, joueurs):
        index = tour % len(joueurs)

        if joueurs[index]["termine"]:
            return get_joueur(tour + 1, joueurs)

        return joueurs[index]
    
    # Cette fonction joue un tour
    def joueur_tour(joueur, grille):
        joueur["tour"] += 1
        print(f"> {joueur['nom']}")
        afficher_grille(grille)

        reponse = get_mot(joueur)
        if reponse is None:
            joueur["termine"] = True
        
        return reponse, joueur["termine"]

    # Cette fonction vérifie qu'une entrée est correcte
    def entree_correcte(val):
        return val.isalpha() and len(val) >= 3

    # Cette fonction récupère le mot entré par un joueur
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
            if not entree_correcte(mot):
                print("Écrivez un mot de 3 lettres ou plus.")
                continue

            return mot

    # Boucle du jeu (tant que le jeu n'est pas terminé)
    while not jeu_termine:
        joueurs, grille = init()

        tour = 0
        # Boucle d'une partie (tant que la partie n'est pas terminée)
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

# jouer(7) # Enlever en commentaire pour jouer une partie




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
            i = 0
            for _ in range(100): 
                try: 
                    grille = generer_grille(rand_num(0, 1000, [3, 4]))
                except InvalidGridSizeException:
                    i += 1   
            assert i == 100
            print(f"    [PASS] Tableau vide généré lorsque la taille n'est pas valide")
        except AssertionError:
            print(f"    <FAIL> Tableau vide généré lorsque la taille n'est pas valide")
        
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
        mots_valide = ["ROI", "DROIT", "CARTE", "GARE", "TRAME", "TORD"]
        try:
            for mot in mots_valide:
                assert est_valide(mot, grille_4) == True
            print(f"    [PASS] Mot est valide si formé de lettres adjacentes (grille 4x4)")
        except AssertionError:
            print(f"    <FAIL> Mot est valide si formé de lettres adjacentes (grille 4x4)")

        mots_valide = ["POUR", "RAGE", "BOURDE", "PUZZLE", "GEL"]
        try:
            for mot in mots_valide:
                assert est_valide(mot, grille_5) == True
            print(f"    [PASS] Mot est valide si formé de lettres adjacentes (grille 5x5)")
        except AssertionError:
            print(f"    <FAIL> Mot est valide si formé de lettres adjacentes (grille 5x5)")
    
    def calcul_point_test():    
        print(f"> Test sur calcul_point()")             

        points_4 = [0, 0, 0, 1, 2, 3, 5, 8, 10]
        for i in range(len(points_4)):
            point = points_4[i]
            try:
                assert calcul_point(rand_word(i), grille_4) == point
                print(f"    [PASS] Mot de {i} lettres retourne {point} points pour une grille 4x4")
            except AssertionError:
                print(f"    <FAIL> Mot de {i} lettres retourne {point} points pour une grille 4x4")
        try:
            point = 10
            for _ in range(8, 100):
                assert calcul_point(rand_word(i), grille_4) == point 
            print(f"    [PASS] Mot de plus de 8 lettres retourne {point} points pour une grille 4x4")
        except AssertionError:
            print(f"    <FAIL> Mot de plus de 8 lettres retourne {point} points pour une grille 4x4")

        points_5 = [0, 0, 0, 1, 2, 3, 4, 6, 10]
        for i in range(len(points_5)):
            point = points_5[i]
            try:
                assert calcul_point(rand_word(i), grille_5) == point
                print(f"    [PASS] Mot de {i} lettres retourne {point} points pour une grille 5x5")
            except AssertionError:
                print(f"    <FAIL> Mot de {i} lettres retourne {point} points pour une grille 5x5")
        
        try:
            point = 10
            for _ in range(8, 100):
                assert calcul_point(rand_word(i), grille_5) == point 
            print(f"    [PASS] Mot de plus de 8 lettres retourne {point} points pour une grille 5x5")
        except AssertionError:
            print(f"    <FAIL> Mot de plus de 8 lettres retourne {point} points pour une grille 5x5")
    
    generer_grille_test()
    est_valide_test()
    calcul_point_test()

test() # Enlever en commentaire pour exécuter les tests
