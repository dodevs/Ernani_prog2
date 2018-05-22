def somaRecursiva(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + somaRecursiva(lista[1:])
    return 0

def produtoRecursivo(x,y): #2,3
    if x == 1:
        return y
    else:
        return produtoRecursivo(x-1,y) + y

def divisaoRecursiva(x,y):#10,2
    subt = x-y #8 #6 #4 #2 #0
    if subt < y:
        return subt #0
    else:
        return divisaoRecursiva(subt,y)


def main():
    print(somaRecursiva([1,2,3]))
    print(produtoRecursivo(3,3))
    print(divisaoRecursiva(50,20))


if __name__ == "__main__":
    main()