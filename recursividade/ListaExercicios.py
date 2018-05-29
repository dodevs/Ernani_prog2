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

#Raiz com método newthon raphson
#Xi = (Xo² + N) / 2 * Xo
#N := 27
#Numero elevado ao quadrado mais proximo de 27: 5 = 5² = 25
#Xo := 5
#Xi = (25 + 27) / 2 * 5
#Xi := 5,2

#Agora o Xi se torna o Xo da proxima aproximação
#Xi = (5,2² + 27) / 2 * 5,2
def raizRecursiva(n,t,xo=0):
    if t == 1:
        Xo = [x for x in range(n)  if (x**2) < n ][-1]
    else:
        Xo = xo
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        Xi = ((Xo ** 2) + n) / (2 * Xo)
        precisao = Xo - Xi
        while i < t
            

        return Xi

def main():
    #print(somaRecursiva([1,2,3]))
    #print(produtoRecursivo(3,3))
    #print(divisaoRecursiva(50,20))
    print(raizRecursiva(27,1))


if __name__ == "__main__":
    main()