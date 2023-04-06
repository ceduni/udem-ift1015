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
    pensize(1)
    pencolor(0,0,0)    
    for _ in range(4):
        fd(cote); lt(90)

def rate(cote):
    pencolor(0, 0.5, 0.5); pensize(2)
    for _ in range(4):
        fd(cote); lt(90)
    hypotenuse = math.sqrt(cote**2 + cote **2)
    lt(45); fd(math.sqrt(cote**2 + cote **2));
    pu(); fd(-math.sqrt(cote**2 + cote **2)); rt(45); pd()
    pu(); fd(cote); pd(); lt(135); fd(hypotenuse);
    pu(); fd(-hypotenuse); rt(135); fd(-cote); pd();     

def touche(cote, espace):
    pensize(4); pencolor(0.8,0.3,0)
    pu(); fd(cote//2 - 1); pd()
    circle(cote//2)
    pu(); fd(-cote//2 + 1); pd()  
    
def index_2_coord(x, y):
    return chr(ord("A") + x) + str(6 - y)

def est_rate(joueur, x, y):
    coord = index_2_coord(x, y)
    return coord in joueur.visite and coord not in joueur.bateau 

def est_touche(joueur, x, y):
    coord = index_2_coord(x, y)
    return coord in joueur.visite and coord in joueur.bateau
 
def positionner(x, y):
    pu(); fd(x); lt(90); fd(y); rt(90); pd()

def grille(cols, lignes, taille, espace, joueur):
    for x in range(cols):
        for y in range(lignes):
            positionner(x * (taille + espace), y * (taille + espace))
            if est_rate(joueur, x, y):
                rate(taille)
            elif est_touche(joueur, x, y):
                touche(taille, espace)
            else:
                carre(taille)
            positionner(-x * (taille + espace), -y * (taille + espace))
            
def termine(joueurs):
    def tout_trouve(joueur):
        for b in joueur.bateau:
            if b not in joueur.visite:
                return False
        return True
    
    for joueur in joueurs:
        if tout_trouve(joueur):
            return True
    return False

def est_coord_valide(coord):
    if len(coord) != 2:
        return False
    return coord[0] in "ABCDEF" and coord[1] in "123456"

def rafraichir(joueurs):
    clear()
    pu();goto(-150,-60);pd()
    grille(6,6,16,4,joueurs[0])
    pu();goto(0,-110);pd()
    lt(90); pensize(10); pencolor(0,0.4,0.8); fd(50 + 20 * 6 + 50); 
    pu(); fd(-(50 + 20 * 6 + 50)); rt(90); pencolor(0,0,0); pd(); 
    pu();goto(40,-60);pensize(1);pd()
    grille(6,6,16,4,joueurs[1])

def creer_joueur():
    list_bateau = []
    while len(list_bateau) < 5:
        x = int(random() * 6)
        y = int(random() * 6)
        coord = index_2_coord(x, y)
        if coord not in list_bateau:
            list_bateau.append(coord)
    # print(list_bateau)
    return struct(bateau= list_bateau, visite= [])

def jouer():
    joueurs = [creer_joueur(), creer_joueur()]
    tour = 1
    rafraichir(joueurs)
    while not termine(joueurs):
        i = (tour + 1) % 2
        adversaire = joueurs[i - 1]
        
        coord = input("Joueur " + str(i+1) + ": ").upper()
        while not est_coord_valide(coord):
            coord = input("Joueur " + str(i+1) + ": ")
        
        adversaire.visite.append(coord)
        
        rafraichir(joueurs)
        tour += 1
        
    print("Joueur " + str(i+1) + " a gagné!")
    
jouer()