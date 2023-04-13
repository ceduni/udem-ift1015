def concat(liste_mots, index, resultat):
    if index == len(liste_mots):
        return resultat
    
    resultat += liste_mots[index]
    return concat(liste_mots, index + 1, resultat)


print(concat(["fin", "de", "session"], 0, ""))
