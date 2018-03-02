def composta(texto, i):


def separaPal(texto):
    #separador = [" ", ".", ",", "!", "?"]
    listaPal = []
    temp = ""
    for i in range(len(texto)):#Eu comi um pe-de-moleque
        if texto[i].isalnum() || texto[i] == '-' && composta(texto, i):
            temp += texto[i]
        elif temp != '':
            listaPal.append(temp)
            temp = ""
    if len(temp) > 0:
        listaPal.append(temp)

    return listaPal

def main():
    texto = 'Eu comi um pe-de-moleque'
    #texto = open('biblia-em-txt.txt','rt').read()
    print(len(separaPal(texto)))

if __name__ == "__main__":
    main()
