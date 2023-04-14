###############################################################################
## Ce programme récupère des inscriptions et les enregistre dans un fichier.
## Les inscriptions sont sauvegardées dans le fichier inscriptions.csv 
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-04-02
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################


def creer_inscription(entree):
    champs = entree.split(";")
    inscription = {
        "nom": champs[0],
        "email": champs[1],
        "tel": champs[2]
    }
    if len(champs) == 4:
        inscription["groupe"] = champs[3]

    return inscription


def format_inscription(inscription):
    return ";".join(inscription.values())


def sauvegarder(inscriptions, path):
    nb_enregistrement = 0
    try:
        with open(path, "ab") as fichier:
            for ins in inscriptions:
                fichier.write((format_inscription(ins) + "\n").encode("utf-8"))
                nb_enregistrement += 1
    except:
        print("Une erreur est survenue lors de l'enregistrement des inscriptions")
    finally:
        return nb_enregistrement


def main(chemin_sauvegarde):
    def est_valide(entree):
        nb_part = entree.count(";")
        return nb_part >= 2 and nb_part <= 3

    inscriptions = []
    entree = ""

    while entree.upper() != "FIN":
        entree = input('Nouv: ')

        if not est_valide(entree):
            print("Cette inscription n'est pas valide.\nChaque champ (nom, adresse courriel, téléphone, groupe) doit être séparé par un point-virgule.")
            continue

        inscription = creer_inscription(entree)
        inscriptions.append(inscription)

    nb_enregistrement = sauvegarder(inscriptions, chemin_sauvegarde)

    if nb_enregistrement == 0:
        print("Aucune inscription n'a été enregistrée")
    elif nb_enregistrement == 1:
        print(f"{nb_enregistrement} inscription a été enregistrée dans le fichier {chemin_sauvegarde}")
    else:
        print(f"{nb_enregistrement} inscriptions ont été enregistrées dans le fichier {chemin_sauvegarde}")


main("inscriptions.csv")
