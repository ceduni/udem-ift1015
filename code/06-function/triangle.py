def triangle(height, char="*", inverse=False):
    if inverse:
        for i in range(height):
            print(" " * (2 * i + 1) + char * (2 * height - (2 * i + 1)))
    else:
        for i in range(height):
            print(char * (2 * i + 1))


triangle(10)
triangle(height=7, inverse=True)
triangle(5, "#")
