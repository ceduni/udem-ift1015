def read_file(path):
    f = open(path, 'rb')
    return f.read().decode('utf-8')

def write_file(path, text):
    f = open(path, 'wb')
    f.write(text.encode('utf-8'))
    f.close()

def split_line(contenu):
    lignes = contenu.split('\n')
    if lignes[-1] == "": # Enlever la dernière ligne si vide
        lignes.pop()
    return lignes

