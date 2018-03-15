from random import uniform

def tabelaM():
    moedas = ["R$","US$","Fr","Rp","Pe$","Mr"]
    tabelaMon = {}
    for i in range(len(moedas)):
        for j in range(len(moedas)):
            if moedas[i] == moedas[j]:
                tabelaMon[(moedas[i], moedas[j])] = 1
            elif (moedas[i], moedas[j]) not in tabelaMon:
                taxaCV = uniform(1.5, 8.90)
                #taxaCV = float(input("Taxa de conversao {} para {}: ".format(moedas[i], moedas[j])))
                tabelaMon[(moedas[i], moedas[j])] = taxaCV
                tabelaMon[(moedas[j], moedas[i])] = taxaCV ** -1

    return tabelaMon

def main():
    tabela = tabelaM()
    print(tabela)

if __name__ == '__main__':
    main()