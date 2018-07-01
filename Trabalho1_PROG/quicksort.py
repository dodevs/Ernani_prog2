import random
import time
#Quicksort variante Lomuto (pivo extrema direita)

def trocar(v, n, m):
    aux = v[n]
    v[n] = v[m]
    v[m] = aux

# É passado o vetor, a posicao de inicio e posicao final
def quicksort(v, start, end):
    if start < end: #condicao de parada
        q = particionar(v, start, end) # encontro o pivo
        quicksort(v, start, q-1) # pivotagem a esquerda (ordena os menores que o pivo)
        quicksort(v, q+1, end) # pivotagem a direita ( ... )

def particionar(v, start, end):
    pivo = v[start] # O pivo é o primeiro elemento da esquerda
    i = start # destino final do pivo
    j = start + 1 #contador para percorrer o restante do pivo
    
    while j <= end:
        if v[j] < pivo:
            i += 1 # detectou um elemento menor que o pivo, incrementa o i
            trocar(v, i, j)
        j += 1 #passa para o proximo elemento

    trocar(v, start, i)

    return i

def main():
    vetor = list(range(1,1000000))
    random.shuffle(vetor)
    #vetor = [2,3,4,1]
    antes = time.time()
    quicksort(vetor, 0, len(vetor)-1)
    depois = time.time()
    total = (depois-antes) * 1000
    print('%0.2fms' % total)

if __name__ == "__main__":
    main()