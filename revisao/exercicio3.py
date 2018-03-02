def separaPal(texto):
    #separador = [" ", ".", ",", "!", "?"]
    listaPal = []
    temp = ""
    for caractere in texto:
        if caractere.isalpha() or caractere.isdigit():
            temp += caractere
        elif temp != '':
            listaPal.append(temp)
            temp = ""
    if len(temp) > 0:
        listaPal.append(temp)

    return listaPal

def main():
    texto = open('biblia-em-txt.txt', 'rt').read()
    #Comentario
    print(len(separaPal(texto)))

if __name__ == "__main__":
    main()
