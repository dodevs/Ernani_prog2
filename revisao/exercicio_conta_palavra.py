def getIndex(conj, elem):
    for i in range(len(conj)):
        if conj[i] == elem:
            return i

def separaPal(texto):
    listaPal = []
    listaPalCont = []
    temp = ""
    for i in range(len(texto)):
        if texto[i].isalnum():
            temp += texto[i]
        elif len(temp) > 0:
            if texto[i] == "-":
                temp += texto[i]
            else:
                if temp not in listaPal:
                    listaPal.append(temp)
                    listaPalCont.append(1)
                else:
                    listaPalCont[getIndex(listaPal, temp)] += 1
                temp = ""

    if len(temp) > 0:
        if temp not in listaPal:
            listaPal.append(temp)
            listaPalCont.append(1)
        else:
            listaPalCont[getIndex(listaPal, temp)] += 1

    return listaPal, listaPalCont

def main():
    texto = "Oeeeeeee"
    #texto = open('biblia-em-txt.txt', 'rt').read()
    result = (separaPal(texto))
    for i in range(len(result[0])):
        print(result[0][i],"|",result[1][i])

if __name__ == "__main__":
    main()
