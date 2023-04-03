def somme(nombres, result):
    if len(nombres) == 0:
        return result
    print(nombres, result)
    num = nombres.pop()
    return somme(nombres, result + num)

print(somme([1, 2, 3, 4], 0))

def somme(nombres):
    result = 0
    for nombre in nombres:
        result += nombre

    return result
