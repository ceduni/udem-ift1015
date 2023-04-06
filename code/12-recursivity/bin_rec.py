def binaire(N):
    if N == 0:
        return ""
    return "" + binaire(N//2) + str(N % 2)


print(binaire(13))
