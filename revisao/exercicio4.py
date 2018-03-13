def separaPal(texto):
    listaPal = []
    temp = ""
    for i in range(len(texto)):#pe-de-moleque
        if texto[i].isalnum():
            temp += texto[i]
        elif len(temp) > 0:
            if texto[i] == "-":
                temp += texto[i]
            else:
                listaPal.append(temp)
                temp = ""

    if len(temp) > 0:
        listaPal.append(temp)

    return listaPal

def main():
    #texto = 'Eu comi um pe-de-moleque'
    texto = open('biblia-em-txt.txt','rt').read()
    print(separaPal(texto))

if __name__ == "__main__":
    main()
