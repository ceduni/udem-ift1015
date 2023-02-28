def valide_fichier(nom_fichier, extension):
    fichier_extension = ""
    begin = False
    for char in nom_fichier:
        if begin:
            fichier_extension += char

        if char == ".":
            fichier_extension = ""
            begin = True

    return fichier_extension.lower() == extension.lower()

print(valide_fichier("hello_world.py", "py"))