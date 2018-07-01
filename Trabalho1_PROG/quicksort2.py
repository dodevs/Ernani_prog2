import random
import time

def partition(lista, incio, fim):
    pivot = lista[fim]
    bottom = incio-1
    top = fim

    done = 0
    while not done:

        while not done:
            bottom = bottom + 1

            if bottom == top:
                done = 1
                break

            if lista[bottom] > pivot:
                lista[top] = lista[bottom]
                break

        while not done:
            top = top-1

            if top == bottom:
                done = 1
                break

            if lista[top] < pivot:
                lista[bottom] = lista[top]
                break

    lista[top] = pivot
    return top

def ordena_quick(lista, inicio, fim):
    if inicio < fim:
        split = partition(lista, inicio, fim)
        ordena_quick(lista, inicio, split-1)
        ordena_quick(lista, split+1, fim)
    else:
        return

vetor = list(range(1,1000000))
random.shuffle(vetor)
antes = time.time()
ordena_quick(vetor,0,len(vetor)-1)
depois = time.time()
total = (depois-antes) * 1000
print('%0.2fms' % total)