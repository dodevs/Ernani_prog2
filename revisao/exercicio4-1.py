def separaPal(texto):
    listaPal = []
    temp = ""
    for i in range(len(texto)):

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
    texto = 'Douglas disse \"O codigo está com bug\"'
    #texto = open('biblia-em-txt.txt','rt').read()
    print(separaPal(texto))

if __name__ == "__main__":
    main()
