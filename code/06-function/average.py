def moyenne(*nombres):
    somme = 0
    for nombre in nombres: somme += nombre
    return somme / len(nombres)

print(moyenne(1,2,3,4))