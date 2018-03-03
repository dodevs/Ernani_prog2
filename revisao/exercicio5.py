def corrente(texto, indice):

    tamanhoP = len(texto)
    resultado = None

    if indice < tamanhoP:
        if texto[indice].isalnum():
            iStart = iEnd = indice
            while iStart > 0 and texto[iStart].isalnum():
                iStart -= 1

            while iEnd < tamanhoP and texto[iEnd].isalnum():
                iEnd += 1

            resultado = texto[iStart:iEnd]

    return resultado

def main():
    texto = "Ontem choveu aqui em casa"
    palavra = corrente(texto, 4)
    print(palavra)

if __name__ == '__main__':
    main()
