###############################################################################
## Ce programme génère une page HTML à partir de données JSON et d'un template.
## Les données sont récupérées dans un dossier /data qui devraient se trouver
## dans le même emplacement que ce script.
###############################################################################
## Auteur: Louis-Edouard LAFONTANT
## Copyright: Copyright 2023, Ceduni
## Licence: MIT
## Version: 1.0.0
## Date: 2023-04-02
## Email: louis.edouard.lafontant@umontreal.ca
###############################################################################


import json

API_URL = 'data/teachers.json'
TEMPLATE_PATH = 'data/template.html'

def get_data(path):
    with open(path, "rb") as data:
        return json.load(data)

def get_template(path):
    with open(path) as file:
        return file.read()

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
        content = get_data(API_URL)
        template = get_template(TEMPLATE_PATH)
        html_fragment = create_fragment(content, template)
        
        html_page = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>"IFT1015 - Programmation I"</title>
</head>

<body>
    <h1>Enseignants du cours IFT1015 (Programmation I)</h1>
    <div class="teachers">
        {html_fragment}
    </div>
</body>
</html>
        """
        with open("index.html", "wb") as page:
            page.write(html_page.encode("utf-8"))
    except IOError as err:
        print("Une erreur est survenue lors de la génération de la page")
        raise SystemExit(err)
    except:
        print("Le programme a rencontré une erreur")

generate()