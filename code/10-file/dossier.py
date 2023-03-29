
import os


EXTENSION_IMAGE = ["jpg", "jpeg", "png", "gif", "tiff"]
EXTENSION_VIDEO = ["mp4", "mov", "wmv", "flv", "mkv"]
EXTENSION_TEXTE = ["txt", "doc", "docx", "rtf", "pdf"]

def get_chemin():
    chemin = input("Entrer un chemin: ")
    while not os.path.isdir(chemin):
        print("Le chemin entré ne correspond pas à un dossier")
        chemin = input("Entrer un chemin: ")

    return chemin

def est_dossier(chemin):
    return os.path.isdir(chemin)

def est_fichier(chemin):
    return os.path.isfile(chemin)

def get_extension(chemin):
    return chemin[chemin.rindex(".") + 1:]

def est_fichier_image(chemin):
    if not est_fichier(chemin):
        return False
    
    extension = get_extension(chemin)
            
    return extension in EXTENSION_IMAGE

def est_fichier_video(chemin):
    if not est_fichier(chemin):
        return False
    
    extension = get_extension(chemin)
            
    return extension in EXTENSION_VIDEO

def est_fichier_texte(chemin):
    if not est_fichier(chemin):
        return False
    
    extension = get_extension(chemin)
            
    return extension in EXTENSION_TEXTE

def dossier(chemin = None):
    if(chemin is None):
        chemin = get_chemin()
    
    nb_images = 0
    nb_videos = 0
    nb_textes = 0
    sous_dossiers = []

    contenu = os.listdir(chemin)
    
    for fichier in contenu:
        chemin_fichier = os.path.join(chemin, fichier)
        if est_dossier(chemin_fichier):
            sous_dossiers.append(fichier)
        elif est_fichier_image(chemin_fichier): nb_images +=1
        elif est_fichier_video(chemin_fichier): nb_videos += 1
        elif est_fichier_texte(chemin_fichier): nb_textes += 1

    print("- images:", nb_images)
    print("- videos:", nb_videos)
    print("- textes:", nb_textes)
    for dossier in sous_dossiers:
        print(">", dossier)

dossier()