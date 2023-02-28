def snake_case(text, separator = " "):
    result = ""
    UNDERSCORE = "_"

    for c in text:
        if c == separator:
            result +=UNDERSCORE
        else:
            result += c

    return result.lower()

print(snake_case("The physchology of everyday things"))

def capitalize(text, separator = " "):
    result = ""
    capital = True

    for c in text:
        if capital:
            result += c.upper()
        else:
            result += c
            
        capital = c == " " or c == "-"

    return result

print(capitalize("The physchology of everyday things"))