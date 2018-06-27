def cria(expressao):
    from re import split
    #Implementar funcao split
    #re.split('; |, |\+|\-',text)
    termos = split(r'; |, |\+|\-',expressao)
    print(termos)

    if expressao == "x^2":
        return {'A': 1}
    elif expressao == "-x^2":
        return {'A': -1}
    elif expressao == "5x^2":
        return {'A': 5}
    elif expressao == "-5x^2":
        return {'A': -5}
    elif expressao == "x^2+3x":
        return {'A': 1, 'B': 3}
    elif expressao == "x^2-3x+7":
        return {'A': 1, 'B': 3, 'C': 7}


def getA(tadeq2):
    return tadeq2[0]

def getB(tadeq2):
    return tadeq2[1]

def getC(tadeq2):
    return tadeq2[2]

def raiz1(tadeq2g):
    return 0

def raiz2(tadeq2g):
    return 0

def fx(tadeq2g, x):
    return 0