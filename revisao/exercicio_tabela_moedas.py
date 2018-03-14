from random import random

def tabelaM():
    moedas = ["R$","US$","Fr","Rp","Pe$","Mr"]
    tabelaMon = {}
    for i in range(len(moedas)):
        for j in range(len(moedas)):
            if moedas[i] == moedas[j]:
                tabelaMon[(moedas[i], moedas[j])] = 1
            else:
                taxaCV = float(input("Taxa de conversao {} para {}: ".format(moedas[i], moedas[j])))
                tabelaMon[(moedas[i], moedas[j])] = taxaCV

    return tabelaMon

def main():
    tabela = tabelaM()
    print(tabela)

if __name__ == '__main__':
    main()