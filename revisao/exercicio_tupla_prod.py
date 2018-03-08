def main():
    conjA = [0,2,3]
    conjB = [0,21,6]
    print(detectaProd(conjA, conjB))

def detectaProd(lstA, lstB):
    tamanho = len(lstA)
    inicio = 1
    tup = ()
    for i in range(tamanho):
        for j in range(inicio, tamanho):
            prod = lstA[i] * lstA[j]
            if prod in lstB:
                tup_temp = (lstA[i], lstA[j], prod)
                tup = tup + (tup_temp,)
        inicio += 1
    return tup

if __name__ == "__main__":
    main()
