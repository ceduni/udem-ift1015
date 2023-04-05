###############################################################################
## Ce programme génère une page HTML à partir de données JSON et d'un template.
## Les données sont récupérées du serveur (externe) avec un appel GET. 
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-04-02
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################


import requests

API_URL = 'https://ceduni.github.io/udem-ift1015/data/teachers.json'
TEMPLATE_PATH = 'template.html'

def get_file(url):
    """Récupère une ressource (fichier) à une adresse URL donnée

    Args:
        url (str): URL de la ressource

    Returns:
        dict: Contenu JSON du fichier
    """
    response = requests.get(url)
    return response.json()

def bind(data, tpl):
    for key, value in data.items():
        tpl = tpl.replace(f"#{key}", value)

    return tpl

def create_fragment(content, template):
    fragment = ""
    for teacher in content:
        fragment += bind(teacher, template)
        fragment += "\n"
    return fragment

def generate():
    try:
        content = get_file(API_URL)
        with open(TEMPLATE_PATH) as file:
            template = file.read()

        html_fragment = create_fragment(content, template)
        page_title = "IFT1015 - Programmation I"
        page_h1 = "Enseignants du cours IFT1015 (Programmation I)"

        html_page = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title}</title>
</head>

<body>
    <h1>{page_h1}</h1>
    <div class="teachers">
        {html_fragment}
    </div>
</body>
</html>
        """
        with open("index.html", "wb") as page:
            page.write(html_page.encode("utf-8"))
    except requests.exceptions.RequestException as err:
        print("Une erreur est survenue lors de la récupération des données")
        raise SystemExit(err)
    except FileNotFoundError as err:
        print("Le fichier n'a pas été trouvé au chemin indiqué")
        raise SystemExit(err)
    except IOError as err:
        print("Une erreur est survenue lors de la génération de la page")
        raise SystemExit(err)
    except:
        print("Le programme a rencontré une erreur")

generate()