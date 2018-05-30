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
    pass

def onList(e, l): #e=3, l=[1,2,3]
    if l == []:
        return False
    elif e == l[0]:
        return True
    else:
        return onList(e,l[1:])

def invertString(s): #teste
    if s == '':
        return ''
    elif len(s) == 1:
        return s
    else:
        return s[-1] + invertString(s[:-1])

def isnatural(s):
    return "Nao implementada"

class maiorRecursivo:
    def __init__(self, l):
        self.maior = l[0]
        self.l = l
        self(self.l, self.maior)
    def __call__(self,l,maior):
        if len(l) == 1:
            if l[0] > maior:
                return l[0]
            else:
                return maior
        else:
            if l[0] >= maior:
                return self(l[1:], l[0])
            else:
                return self(l[1:], maior) 
    def __str__(self):
        return str(self.maior)

def main():
    #print(somaRecursiva([1,2,3]))
    #print(produtoRecursivo(3,3))
    #print(divisaoRecursiva(50,20))
    #print(raizRecursiva(27,1))
    #print(onList(0,[1]))
    #print(invertString('maquina'))
    maior = maiorRecursivo([0,1,2,3])
    print(maior)

if __name__ == "__main__":
    main()