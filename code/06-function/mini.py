somme = 0
n = 0
while True:
    entree = input(" Entrez le nombre positif #" + str(n + 1))

    if entree == None:
        break
    nombre = float(entree)
    if nombre > 0:
        somme += nombre
        if n > 0:
            valMin = min(valMin, nombre)
            valMax = max(valMax, nombre)
        else:
            valMin = nombre
            valMax = nombre
            n += 1

        if n > 0:
            print("la moyenne est ", somme / n)
            print(" min =", valMin, " max =", valMax)
