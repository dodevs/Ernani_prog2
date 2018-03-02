def main():
    conjA = [7,2,3]
    conjB = [14,21,6]
    print(detectaProd(conjA, conjB))

def detectaProd(lstA, lstB):
    tamanho = len(lstA)
    inicio = 1
    lstI = []
    for i in range(tamanho):
        for j in range(inicio, tamanho):
            prod = lstA[i] * lstA[j]
            if prod in lstB:
                lstI.append([lstA[i], lstA[j], lstB[lstB.index(prod)]])
        inicio += 1
    return lstI

if __name__ == "__main__":
    main()
