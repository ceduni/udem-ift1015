phrase = "Bonjour Okhri, aujourd'hui nous ferons notre 3e demonstration"

nb_caracteres = len(phrase)
nb_mots = 0
nb_mots_long = 0
nb_mots_complexe = 0
nb_ponctuations = 0

consonnes = "bcdfghjklmnpqrstvwxyz"
mot = ""

def analyse_mot(mot):
    global nb_mots_complexe
    
    compteur_consonne = 0
    for c in mot:
        if compteur_consonne > 3:
            nb_mots_complexe += 1
            break
        if c in consonnes:
            compteur_consonne += 1
        else:
            compteur_consonne = 0

for w in phrase:
    if(w == " "):
        nb_mots += 1
        if len(mot) > 7:
            nb_mots_long += 1

        analyse_mot(mot)        
        mot = ""
    elif(w == "," or w == ";"):
        nb_ponctuations += 1
    else:
        mot += w
        
if(len(mot) > 0):
    analyse_mot(mot)
    nb_mots += 1

def report():
    print("RAPPORT D'ANALYSE")
    print("Nombre de mots:", nb_mots)
    print("Nombre de caractères:", nb_caracteres)
    print("Nombre de mots de plus de 7 caractères:", nb_mots_long)
    print("Nombre de mots avec plus de 3 consonnes successives:", nb_mots_complexe)
    print("Nombre de ponctuations:", nb_ponctuations)