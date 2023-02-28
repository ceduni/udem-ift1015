def renverse (mot):
    result = ""
    for c in mot:
        result = c + result

    return result

print(renverse("leon"))