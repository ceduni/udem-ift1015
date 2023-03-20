###############################################################################
## Ce programme permet de jouer au jeu de mots Wordle (en français)
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-03-08
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################

from random import random

LIST_OF_WORDS = [
    "campa", "nopas", "aimes", "porto", "dîner", "quota", "rompe", "brélé", "blets", "doués", "seuil", "noces", "comté", "rangs", "murât", "béate", "duces", "éprit",
    "seaux", "bâtai", "crène", "cabré", "navet", "fovéa", "cavez", "délié", "jouer", "avéra", "ridée", "échos", "roder", "grise", "cossu", "avère", "mûtes", "écura",
    "suant", "parié", "dorée", "peint", "rhuma", "juive", "rouît", "vanne", "mêles", "pensa", "fétus", "avéré", "lofer", "guéri", "gémis", "gazés", "oxyda", "kache",
    "piffé", "islam", "toqua", "mélia", "adent", "salée", "pinte", "dînes", "écime", "rater", "bangs", "bisez", "liard", "visée", "amusé", "cuira", "surit", "gnôle",
    "tubât", "rashs", "gypse", "mater", "musas", "gâtât", "faire", "pelas", "ôtant", "touai", "cille", "guipé", "muons", "chers", "havés", "guéas", "muets", "cacao",
    "tinté", "ardue", "gaine", "lapés", "galbe", "écart", "passé", "égare", "gonde", "gâtés", "aient", "halbi", "pille", "radez", "miser", "semas", "potes", "bruma",
    "acnés", "durée", "tries", "traça", "lotit", "pénal", "mûrit", "grèse", "épais", "bicha", "sapât", "réels", "brode", "garou", "proie", "métas", "scout", "mocos",
    "haves", "actas", "magna", "outra", "halls", "brada", "futée", "crins", "semis", "mutée", "axais", "râlât", "butor", "aunes", "pêche", "filma", "alpax", "globe",
    "élude", "karma", "douro", "fêtés", "pilés", "imite", "green", "parut", "toqué", "minus", "sapés", "clams", "limes", "appel", "mâche", "filme", "scias", "jadis",
    "calfs", "cirés", "catin", "brick", "litez", "lysât", "gazai", "soudé", "lande", "jetai", "tanks", "argot", "clame", "carié", "mimât", "rager", "béryl", "damné",
    "pomma", "gurus", "tommy", "huché", "cajou", "rimer", "moere", "guète", "gaves", "parée", "bonde", "hâtés", "nuait", "hante", "lapis", "remît", "tango", "figés",
    "arête", "reçût", "stand", "égalé", "velds", "plies", "halai", "cavât", "quipu", "colts", "pilet", "ligue", "errer", "étaux", "dotée", "crépu", "viras", "ligna",
    "jumel", "derme", "salit", "bûcha", "cubée", "agate", "sabré", "bancs", "lapin", "tapie", "chier", "ruade", "bigue", "gênai", "miels", "rogna", "gravé", "éboua",
    "dénue", "cules", "butât", "venez", "liant", "rouez", "bains", "merda", "levât", "iambe", "banné", "oints", "gémie", "sciât", "drope", "fixez", "fécal", "sprat",
    "lapez", "lobes", "herba", "clora", "acter", "moire", "opine", "saqué", "joint", "caves", "coxal", "cumin", "calos", "amuïr", "penné", "plèbe", "neuve", "mitan",
    "meute", "dormi", "frété", "tends", "dopât", "fugua", "nuais", "laids", "indue", "écria", "china", "bâcle", "votés", "réagi", "judos", "luxes", "motus", "grésa",
    "menin", "dûmes", "nitre", "taupé", "laina", "tapes", "mètre", "anode", "quark", "rodât", "jurat", "hocha", "casas", "rasât", "égout", "acéra", "sigle", "mimés",
    "devez", "veuve", "pacte", "pétré", "pètes", "fuira", "andin", "lochs", "pavât", "gigue", "épieu", "tôlée", "vagué", "tubai", "prend", "éclat", "bonds", "trône",
    "nagée", "déçût", "diode", "juger", "petit", "mussa", "piffe", "folle", "doper", "baisa", "stout", "tillé", "broya", "bisât", "gâtai", "niche", "sucre", "gavât",
    "semer", "farda", "macre", "luxât", "tarât", "cilla", "merde", "codai", "senne", "fions", "celai", "hable", "rodez", "gamet", "gérez", "tiens", "crans", "chiés",
    "jacte", "âcres", "axiez", "velue", "cités", "épair", "sushi", "régit", "stage", "blâma", "gansa", "avens", "ahana", "forma", "stéré", "roser", "bâtît", "zooms",
    "germé", "assez", "tâché", "lamai", "apion", "gobas", "remis", "bâtés", "cuber", "laqué", "ocrer", "guidé", "yèble", "bilan", "papes", "grime", "maria", "relié",
    "buscs", "brayé", "athée", "gîter", "pesés", "slows", "bissé", "fonda", "jabla", "jambe", "fraye", "angor", "dupai", "inuit", "roulé", "rente", "bavât", "forât",
    "élida", "jotas", "typât", "muids", "supin", "delco", "mégot", "régie", "ansée", "bayer", "silos", "jeter", "pausa", "saxos", "tatas", "élime", "necks", "tamis",
    "geint", "stade", "laine", "gorgé", "garda", "rémiz", "lèche", "remua", "gaver", "aviez", "gerbé", "pites", "pipes", "czars", "facho", "phone", "nabot", "houez",
    "carré", "lysat", "tarse", "porté", "aidât", "gruge", "pians", "roche", "geste", "slips", "trêve", "repli", "carpe", "loger", "coron", "normé", "pipai", "chias",
    "argon", "malle", "bogue", "baver", "monel", "drame", "fêler", "prose", "coulé", "hydre", "délie", "pilon", "baugé", "signé", "hélés", "tacot", "durit", "pissa",
    "émise", "moyen", "drège", "pampa", "digit", "dînât", "remué", "coqué", "amure", "aines", "groin", "glaça", "tracs", "urina", "rôtir", "ladre", "boudé", "rogué",
    "thune", "métra", "fiers", "cajun", "blasé", "émeri", "ratés", "bruît", "poncé", "payer", "farci", "urane", "houes", "cotît", "veine", "chips", "gréée", "dalot",
    "pâmez", "jupes", "paver", "douée", "boume", "capte", "varia", "dégel", "rampe", "inlay", "dallé", "viols", "kiwis", "visât", "fèves", "lacté", "ongle", "objet",
    "obvie", "torve", "tollé", "rions", "rudes", "nopal", "balte", "tabla", "décor", "palma", "préau", "jodle", "typos", "nacré", "fusel", "épiât", "offre", "luron",
    "herse", "damai", "créas", "plats", "liées", "sauré", "rosez", "séché", "maint", "écrié", "binez", "tutti", "foiré", "hâlée", "ponté", "guère", "nagez", "liste",
    "mâles", "jeeps", "sauta", "tords", "fiscs", "percé", "bonne", "félin", "tordu", "rimez", "radés", "aérés", "rénal", "amère", "fèces", "sèvre", "fusse", "baffé",
    "tarie", "sapez", "houés", "larde", "enfer", "torii", "frits", "clava", "villa", "poids", "matte", "joies", "fuies", "pietà", "ville", "mythe", "rôdas", "raque",
    "fanée", "solen", "mûrît", "rôtît", "pagne", "bègue", "plouc", "viles", "étiez", "carry", "caner", "asque", "rugît", "bagne", "sellé", "renne", "tonds", "épila",
    "frocs", "gelât", "hâtas", "étaye", "écule", "genet", "pives", "axant", "lotos", "rumex", "vouer", "puait", "aidez", "routa", "virer", "lance", "menés", "ruons",
    "soute", "jutât", "toise", "vertu", "reput", "celas", "crête", "verso", "quels", "mutes", "égide", "vinai", "fêtas", "émeus", "émaux", "taxez", "panax", "forcé",
    "roidi", "varie", "capot", "forez", "papas", "surir", "agave", "carde", "subit", "tâtez", "misée", "farce", "osons", "tonde", "fanai", "nordi", "périt", "ouvre",
    "bougé", "cycle", "jurai", "pâmât", "dédît", "jetas", "jouez", "lutin", "cotez", "guéée", "cyans", "bavai", "surît", "beaux", "humez", "séant", "gauss", "foncé",
    "avals", "celât", "toril", "pâlît", "ondes", "haies", "avide", "tilla", "réiez", "vélar", "neige", "lofts", "vîtes",
]

def generate_word():
    """Cette fonction retourne un mot alétoirement choisi de la liste de mots

    Returns:
        string: Mot aléatoire (formaté) de la liste 
    """
    rand_index = int(random() * len(LIST_OF_WORDS))
    word = LIST_OF_WORDS[rand_index]
    return format_word(word)

def is_valid_word(word):
    """Cette fonction retourne un booléen indiquant si un mot est valide (composé de 5 lettres).

    Args:
        word (string): Mot à valider

    Returns:
        bool: Booléen indiquant si le mot est valide
    """
    return len(word) == 5 and word.isalpha()

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

def eval_word(hword, pword):
    """Cette fonction évalue le mot proposé (pword) en fonction du mot à deviner (hword).

    Args:
        hword (string): Mot à deviner
        pword (string): Mot proposé

    Returns:
        bool: Booléen indiquant si le mot proposé est égal au mot à deviner (mot trouvé)
    """

    if hword == pword:
        return True

    for c in pword:
        print("[" + c + "]", end="")

    print()

    found = ""
    for index, c in enumerate(pword):
        if index < len(hword) and c == hword[index]:
            print("[" + c + "]", end="")
            found += c
        elif c not in found and c in hword:
            print("[!]", end="")
        else:
            print("[x]", end="")

    print()

    return False


NB_TENTATIVES_MAX = 6

# Fonction principale du programme
# Cette fonction débute une partie et fait le suivi des propositions
def play():
    hidden_word = generate_word()
    
    nb_attempt = 0
    won = False

    def over():
        return won or nb_attempt >= NB_TENTATIVES_MAX

    while not over():
        guess = input("Tentative #" + str(nb_attempt + 1) + ": ")

        if not is_valid_word(guess):
            print("Écrivez un mot de 5 lettres.")
            continue

        guess = format_word(guess)

        won = eval_word(hidden_word, guess)

        nb_attempt += 1

    if won:
        print("GAGNÉ!")
    else:
        print("Perdu! Le mot est: " + hidden_word)

play()



#################################################################################
# Tests unitaires
#################################################################################

def test():
    LIST_OF_WORDS_FORMATTED = []

    for word in LIST_OF_WORDS:
        LIST_OF_WORDS_FORMATTED.append(format_word(word))

    def rand_word():
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        word = ""
        for _ in range(5): word += letters[int(random() * len(letters))]
        return word

    def generate_word_test():
        for _ in range(100): assert generate_word() in LIST_OF_WORDS_FORMATTED
        for _ in range(100): assert is_valid_word(generate_word())
    
    def is_valid_word_test():
        for _ in range(100): assert is_valid_word(rand_word()) == True
        for word in ["abcdef", "a", "ab", "abc", "abcd", ""]: assert is_valid_word(word) == False
        assert is_valid_word("ab cde") == False
        assert is_valid_word("ab-de") == False
        assert is_valid_word("12345") == False
    
    def format_word_test():
        assert format_word("abcde") == "ABCDE"
        assert format_word("ABCDE") == "ABCDE"
        assert format_word("éèêëe") == "EEEEE"
        assert format_word("àâùûô") == "AAUUO"
        assert format_word("dorée") == "DOREE"
        assert format_word("dédît") == "DEDIT"
        assert format_word("déçût") == "DECUT"
        assert format_word("mètre") == "METRE"

    generate_word_test()
    is_valid_word_test()
    format_word_test()

# test() # Enlever en commentaire pour exécuter les tests
