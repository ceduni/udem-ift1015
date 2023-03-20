###############################################################################
## Ce programme permet de naviguer à travers une liste de films en utilisant
## une entrée de l'utilisateur (version sans import)
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-03-08
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################



# Liste de films
FILMS = [
    {
        "title": "Godland",
        "summary": "In the late 19th century, a young Danish priest travels to a remote part of Iceland to build a church and photograph its people. But the deeper he goes into the unforgiving landscape, the more he strays from his purpose, the mission and morality.",
        "genre": ["Drama"],
        "length": 138,
        "release_date": "2022-05-24",
        "director": ["Hlynur Pálmason"],
        "cast": ["Elliott Crosset Hove", "Ingvar Sigurdsson", "Vic Carmen Sonne", "Jacob Lohmann", "Hilmar Guðjónsson", "Waage Sandø"],
        "country":	["Denmark", "Iceland", "France", "Sweden"],
        "language":	["Icelandic", "Danish"],
        "featured": False
    },
    {
        "title": "As Bestas (The Beasts)",
        "summary": "A middle-aged French couple moves to a local village, seeking closeness with nature where their presence inflames two locals to the point of outright hostility and shocking violence.",
        "genre": ["Drama", "Thriller"],
        "length": 137,
        "release_date": "2022-07-20",
        "director": ["Rodrigo Sorogoyen"],
        "cast": ["Denis Ménochet", "Marina FoÏs", "Luis Zahera", "Diego Anido", "Marie Colomb"],
        "country":	["Spain", "France"],
        "language":	["French", "Spanish", "Galician"],
        "featured": True
    },
    {
        "title": "Champions",
        "summary": "A former minor-league basketball coach is ordered by the court to manage a team of players with intellectual disabilities. He soon realizes that despite his doubts, together, this team can go further than they ever imagined.",
        "genre": ["Comedy"],
        "length": 124,
        "release_date": "2023-03-10",
        "director": ["Bobby Farrelly"],
        "cast": ["Woody Harrelson", "Kaitlin Olson", "Ernie Hudson", "Cheech Marin"],
        "country":	["United States"],
        "language":	["English"],
        "featured": False
    },
    {
        "title": "65",
        "summary": "After a catastrophic crash on an unknown planet, pilot Mills quickly discovers he's actually stranded on Earth 65 million years ago. Now, with only one chance at rescue, Mills and the only other survivor, Koa, must make their way across an unknown terrain riddled with dangerous prehistoric creatures in an epic fight to survive.",
        "genre": ["Sci-Fi"],
        "length": 93,
        "release_date": "2023-03-10",
        "director": ["Scott Beck", "Bryan Woods"],
        "cast": ["Adam Driver", "Ariana Greenblatt", "Chloe Coleman"],
        "country":	["United States"],
        "language":	["English"],
        "featured": False
    },
    {
        "title": "Brother",
        "summary": "Brother is the story of Francis and Michael, sons of Caribbean immigrants maturing into young menamidst Toronto's pulsing 1990's hip-hop scene. A mystery unfolds when escalating tensions set off aseries of events which changes the course of the brothers' lives forever.",
        "genre": ["Drama"],
        "length": 119,
        "release_date": "2023-03-17",
        "director": ["Clement Virgo"],
        "cast": ["Lamar Johnson", "Aaron Pierre", "Kiana Madeira", "Lovell Adams-Gray & Marsha Stephanie Blake"],
        "country": ["Canada"],
        "language":	["English"],
        "featured": False
    },
    {
        "title": "Creed III",
        "summary": "After dominating the boxing world, Adonis Creed has been thriving in both his career and family life. When a childhood friend and former boxing prodigy, Damian, resurfaces after serving a long sentence in prison, he is eager to prove that he deserves his shot in the ring.",
        "genre": ["Drama", "Sports"],
        "length": 116,
        "release_date": "2023-03-03",
        "director": ["Michael B. Jordan"],
        "cast": ["Michael B. Jordan", "Tessa Thompson", "Jonathan Majors", "Wood Harris", "Florian Munteanu", "Phylicia Rashad"],
        "country": ["United States"],
        "language":	["English"],
        "featured": True
    },
    {
        "title": "John Wick: Chapter 4",
        "summary": "John Wick uncovers a path to defeating the High Table, but before he can earn his freedom, Wick must face off against a new enemy with powerful alliances across the globe and forces that turn old friends into new foes.",
        "genre": ["Action", "Crime", "Thriller"],
        "length": 169,
        "release_date": "2023-03-24",
        "director": ["Chad Stahelski"],
        "cast": ["Keanu Reeves", "Donnie Yen", "Bill Skarsgård", "Laurence Fishburne", "Hiroyuki Sanada", "Shamier Anderson", "Lance Reddick", "Ian McShane"],
        "country": ["United States"],
        "language":	["English"],
        "featured": False
    },
    {
        "title": "The Super Mario Bros. Movie",
        "summary": "Based on the Nintendo video game franchise Mario. With help of Princess Peach, Mario gets ready to square off against the all-powerful Bowser to stop his plans.",
        "genre": ["Action", "Adventure", "Adaptation", "Animated"],
        "length": 92,
        "release_date": "2023-03-24",
        "director": ["Aaron Horvath", "Michael Jelenic"],
        "cast": ["Chris Pratt", "Charlie Day", "Jack Black", "Anya Taylor-Joy", "Keegan-Michael Key", "Seth Rogen"],
        "country": ["United States", "Japan"],
        "language":	["English"],
        "featured": False
    },
    {
        "title": "My Neighbor Totoro",
        "summary": "My Neighbor Totoro is a deceptively simple tale of two girls, Satsuki and Mei, who move with their father to a new house in the countryside. They soon discover that the surrounding forests are home to a family of Totoro's, gentle but powerful creatures who live in a huge and ancient camphor tree and are seen only by children.",
        "genre": ["Animation", "Anime", "Fantasy"],
        "length": 98,
        "release_date": "1988-04-16",
        "director": ["Hayao Miyazaki"],
        "cast": ["Hitoshi Takagi", "Noriko Hidaka", "Chika Sakamoto"],
        "country": ["Japan"],
        "language":	["Japanese"],
        "featured": True
    }
]

# Cette fonction formate le temps (en minutes) en heure et minute


def format_time(t):
    h = t // 60
    min = t % 60

    if h == 0:  # Si le nombre d'heure est de 0, il n'est pas nécessaire de l'afficher
        return str(t) + "min"
    else:
        # `zfill` assure que les minutes s'inscriveront toujours avec 2 chiffres
        return str(h) + "h" + str(min).zfill(2) + "min"


def display_plural(arr, sing, plur):
    if len(arr) == 1:
        print(f'{sing}: {"".join(arr)}')
    else:
        print(f'{plur}: {", ".join(arr)}')


def display(film):
    print(f'- {film["title"]} | Sortie le:{film["release_date"]}')
    print(f'  {format_time(film["length"])} - {", ".join(film["genre"])}')
    display_plural(film["language"], "  Langue", "  Langues")


def display_full(film):
    print(f'{film["title"]} | Sortie le:{film["release_date"]}')
    print(f'{format_time(film["length"])} - {", ".join(film["genre"])}')
    display_plural(film["language"], "Langue", "Langues")
    print(f'{film["summary"]}')
    display_plural(film["director"], "Directeur", "Directeurs")
    print(f'Cast: {", ".join(film["cast"])}')


def shuffle(arr):
    insert_index = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            temp = arr.pop(i)
            arr.insert(insert_index, temp)
            insert_index += 1


def rotate_left(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i] 
    arr[-1] = temp


def rotate_right(arr):
    temp = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        arr[i+1] = arr[i] 
    arr[0] = temp


def get_featured_films():
    featured = []
    for film in FILMS:
        if film["featured"]:
            featured.append(film)
    
    return featured


# Cette fonction "efface" tout ce qu'il y a dans le terminal (console) en ajoutant des espaces


def clear_console():
    for _ in range(10):
        print()


def main():
    featured_films = get_featured_films()
    shuffle(FILMS)
    while True:
        print("À ne pas manquer\n")
        for film in featured_films:
            display(film)
            print()
        
        print("FILMS")
        display_full(FILMS[0])
    
        print("\n")
        key = input("[J]-Precedent [L]-Suivant        [Q]:Quitter").upper()

        if key == "J":
            rotate_left(FILMS)
            display(FILMS[0])
        elif key == "L":
            rotate_right(FILMS)
            display(FILMS[0])
        elif key == "Q":
            print("Merci d'avoir utilisé ciné-campus+")
            break
        else:
            print("Veuillez entre 'J' pour aller au film précédent, 'L' pour aller au film suivant et 'Q' pour quitter Cine-campus+")

        clear_console()  # Nettoie l'écran

main() # Exécute le programme


def test():
    def format_time_test():
        def eval_test(t, expect):
            actual = format_time(t)
            msg = f"format_time({t}) => '{actual}' | Valeur attendue: '{expect}'"
            assert actual == expect, msg

        eval_test(0, "0min")
        eval_test(15, "15min")
        eval_test(45, "45min",)
        eval_test(60, "1h00min")
        eval_test(95, "1h35min")
        eval_test(140, "2h20min")

    def shuffle_test():
        def eval_test(arr, expect):
            copy = arr.copy()
            shuffle(arr)
            msg = f"shuffle({copy}) => '{arr}' | Valeur attendue: '{expect}'"
            assert arr == expect, msg

        eval_test([1, 2, 3, 4, 5, 6], [1, 3, 5, 2, 4, 6])
        eval_test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
        eval_test([1, {"a": 2}, 3], [1, 3, {"a": 2}])
        
    def rotate_left_test():
        def eval_test(arr, expect, n = 1):
            copy = arr.copy()
            for _ in range(n): rotate_left(arr)
            msg = f"rotate_left({copy}) => '{arr}' | Valeur attendue: '{expect}'"
            assert arr == expect, msg

        eval_test([1], [1])
        eval_test([1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 1])
        eval_test([1, 2, 3, 4, 5, 6], [4, 5, 6, 1, 2, 3], 3)
        eval_test([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 6)

    def rotate_right_test():
        def eval_test(arr, expect, n = 1):
            copy = arr.copy()
            for _ in range(n): rotate_right(arr)
            msg = f"rotate_right({copy}) => '{arr}' | Valeur attendue: '{expect}'"
            assert arr == expect, msg

        eval_test([1], [1])
        eval_test([1, 2, 3, 4, 5, 6], [6, 1, 2, 3, 4, 5])
        eval_test([1, 2, 3, 4, 5, 6], [4, 5, 6, 1, 2, 3], 3)
        eval_test([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 6)


    format_time_test()
    shuffle_test()
    rotate_left_test()
    rotate_right_test()


# test()  # Exécute les tests