###############################################################################
## Ce programme extrait et normalise les numéros de téléphone présents dans un
## texte en conservant uniquement les chiffres. 
## Un numéro de téléphone est composé de 7 ou 10 chiffres et chaque bloc de 
## chiffres peut être séparé d'un espace ou d'un trait. 
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-04-13
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

import re

EVENTS = [
    "Rocket de Laval vs. Syracuse Crunch; Place Bell, Laval; 2023-02-14 7:00 PM",
    "Roxane Bruneau; Bell Centre, Montreal; 2023-03-14 8:00 PM",
    "Paraleven; Newspeak, Montreal; 2023-04-14 10:00 PM",
    "Barely Alive; Le Studio TD, Montreal; 2023-04-15 10:00 PM",
    "Paul Piché; Salle Desjardins, Théâtre du Vieux Terrebonne, Terrebonne; 2023-04-15 8:00 PM",
    "Matt Andersen; Club Soda, Montreal; 2023-04-25 8:00 PM",
    "Festival Brewtal 2023 - Clutch; MTELUS, Montreal; 2023-05-12 8:00 PM",
    "Suzane; Le Studio TD, Montreal; 2023-06-05 8:00 PM",
    "Adriatique; Société Des Arts Technologiques (SAT), Montreal; 2023-06-21 10:00 PM",
]

DATE_REGEX = re.compile(r'(\d{4})-(\d{2})-(\d{2})') # Expression utilisée pour extraire une date
REQ_DATE_REGEX = re.compile(r'LE (\?|\d{4})-(\?|\d{2})-(\?|\d{2})') # Expression utilisée pour extraire une requête de date
REQ_PERIODE_REGEX = re.compile(r'ENTRE (\d{4}-\d{2}-\d{2}) ET (\d{4}-\d{2}-\d{2})') # Expression utilisée pour extraire une requête de période


# Cette fonction retourne toutes les correspondances d'une requete de type date.
# Elle retourne tous les évènements où la date correspond à la date spécifiée dans la requête
def trouve_event_date(req):
    events_date = [] 
    an_req, mois_req, jour_req = REQ_DATE_REGEX.search(req).groups()
    for event in EVENTS:
        title, venue, datetime = event.split(";") 
        an_date, mois_date, jour_date  = DATE_REGEX.search(datetime).groups()

        if an_req == "?" or an_req == an_date:
            if mois_req == "?" or mois_req == mois_date:
                if jour_req == "?" or jour_req == jour_date:
                    events_date.append(event)

    return events_date


# Cette fonction compare 2 dates (date1, date2) et retourne
# 1 (date1 > date2), 0 (date1 = date2) ou -1 (date1 < date2) 
def comp_date(date1, date2):
    date1_an, date1_mois, date1_jour = date1.split("-")
    date2_an, date2_mois, date2_jour = date2.split("-")

    if date1 == date2: return 0
    if int(date1_an) < int(date2_an): return -1
    if int(date1_an) > int(date2_an): return 1
    if int(date1_mois) < int(date2_mois): return -1
    if int(date1_mois) > int(date2_mois): return 1
    if int(date1_jour) < int(date2_jour): return -1
    if int(date1_jour) > int(date2_jour): return 1
    

# Cette fonction retourne toutes les correspondances d'une requete de type période.
# Elle retourne tous les évènements où la date est comprise dans la période spécifiée dans la requête
def trouve_event_periode(req):
    events_periode = [] 
    debut_req = REQ_PERIODE_REGEX.search(req).group(1)
    fin_req = REQ_PERIODE_REGEX.search(req).group(2)
    for event in EVENTS:
        title, venue, datetime = event.split(";")
        date  = DATE_REGEX.search(datetime).group()

        if comp_date(date, debut_req) >= 0  and comp_date(date, fin_req) <= 0:
            events_periode.append(event)

    return events_periode

# Cette fonction vérifie qu'une requête est de type date
def est_req_date(entree):
    return REQ_DATE_REGEX.search(entree) is not None

# Cette fonction vérifie qu'une requête est de type période
def est_req_periode(entree):
    return REQ_PERIODE_REGEX.search(entree) is not None

# Cette fonction vérifie qu'une requête est valide (type date ou période)
def est_req_valide(entree):
    return est_req_date(entree) or est_req_periode(entree)

# Cette fonction retourne le type de la requête
def type_requete(entree):
    if entree.startswith("LE"): return "date"
    if entree.startswith("ENTRE"): return "periode"


# Fonction principale
def demarrer():
    entree = ""

    while True:
        entree = input('> ').upper().strip()

        if entree.upper() == "MERCI":
            break

        if not est_req_valide(entree):
            print("Cette requête n'est pas valide.")
            continue

        match type_requete(entree):
            case "date": print(trouve_event_date(entree))
            case "periode": print(trouve_event_periode(entree))

demarrer()