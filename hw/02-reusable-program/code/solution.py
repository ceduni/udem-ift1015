###############################################################################
## Ce programme calcule le montant des versements mensuel pour rembourser un 
## prêt hypothécaire
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-02-12
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

# Fonction secondaire réalisant l'affichage de l'accélération

NB_VERSEMENTS = 12

def versement_mensuel(pret, taux, annee):
    interet = interet_mensuel(taux)
    versement = pret * interet / (1 - ( 1 + interet) ** (-NB_VERSEMENTS * annee) )

    return round(versement, 2)

def interet_mensuel(taux):
    return taux / NB_VERSEMENTS

def isnumber(val):
    return val.isdigit() and int(val) > 0

def ispercentage(val):
    return val.replace('.', '', 1).isdigit() and float(val) > 0 and float(val) < 100


def echelonnement(pret, versement, interet, annee):
    TOTAL_VERSEMENTS = NB_VERSEMENTS * annee
    balance = float(pret)
    print("Echelonnement des versements (par mois)")
    print("-----------------------------------------------------------")
    for i in range(TOTAL_VERSEMENTS):
        interet_paye = round(balance * interet, 2)
        montant_paye = round(versement - interet_paye, 2)

        print("{0}) Balance: {1} $ -- Versement: {2} $ ({3} $)".format(i +1, balance, interet_paye, montant_paye))
        balance -= montant_paye
        balance = round(balance, 2)


# Fonction principale réalisant le calcul de l'accélération

def main():
    valid = False
    
    print("ESTIMATEUR DE VERSEMENT HYPOTHÉCAIRE")

    while not valid:
        pret = input("Montant du prêt: ")
        if not isnumber(pret):
            print("Le montant du prêt doit être un nombre positif")
            continue
        pret = int(pret)
        
        annee = input("Durée du prêt: ")
        if not isnumber(annee):
            print("Le nombre d'années doit être un nombre positif")
            continue
        annee = int(annee)
        
        taux = input("Taux d'intérêt: ")
        if not ispercentage(taux):
            print("Le taux d'intérêt doit être un pourcentage")
            continue
        taux = float(taux)/100.0

        valid = True


    versement = versement_mensuel(pret, taux, annee)
    interet = interet_mensuel(taux)
    print("\n> VERSEMENT MENSUEL: {0} $".format(versement))
    print()
    echelonnement(pret, versement, interet,annee)

# main()


# Fonction simulant deux cas de test

def test():
    print(versement_mensuel(90000, 0.075, 20))
    print(versement_mensuel(100000, 0.05, 15))
    print(versement_mensuel(100000, 0.10, 20))
    print(versement_mensuel(60000, 0.065, 5))
    print(versement_mensuel(65000, 0.08, 10))


test() # Exécution des tests