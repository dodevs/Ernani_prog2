def corrente(texto, indice):

    tamanhoP = len(texto)
    resultado = None

    if indice < tamanhoP and indice > 0:
        if texto[indice].isalnum():
            iStart = iEnd = indice
            while iStart - 1 > 0 and texto[iStart - 1].isalnum():
                iStart -= 1

            while iEnd < tamanhoP and texto[iEnd].isalnum():
                iEnd += 1

            resultado = texto[iStart:iEnd]

    return resultado

def main():
    texto = "a"
    palavra = corrente(texto, 0)
    print(palavra)

if __name__ == '__main__':
    main()
