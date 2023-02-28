def camel_case(text, separator = " -"):
    result = ""
    capital = False

    for c in text:
        if capital:
            result += c.upper()
        elif c in separator:
            result += ""
        else:
            result += c
            
        capital = c == " " or c == "-"

    return result

print(camel_case("The physchology of everyday things"))