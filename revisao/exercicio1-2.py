'''
    Exercicio de revisao 1 (uniao)
    Criar um algoritmo para retornar a uniao de duas listas

    Exercicio de revisao 2 (intersecao)
    Criar um algoritmo para retornar a intersecao de duas listas
'''
def intersecao(listaA, listaB):
    listaAIB = []
    #somente adiciona a listaA os termos que se repetem
    listaAIB.extend([item for item in listaA if(item in listaB)])
    return listaAIB

def uniao(listaA, listaB):
    listaAUB = []

    for i in range(len(listaA)):
        listaAUB.append(listaA[i])

    #somente adiciona a listaA os termos que nao se repetem
    listaAUB.extend( [item for item in listaB if not(item in(listaAUB))])
    return listaAUB

def main():
    listaA = [1,3,5,7]
    listaB = [2,1,3,5]
    print(uniao(listaA, listaB))
    print(intersecao(listaA, listaB))

if __name__ == '__main__':
    main()
