def separa_pal(line):
    temp = ''
    lista = []
    for i in range(len(line)):
        if line[i] != ' ':
            temp += line[i]
        elif len(temp) > 0:
            striped_temp = temp.strip()
            striped_temp = float(striped_temp)
            lista.append(striped_temp)
            temp = ''
    if len(temp) > 0:
        striped_temp = temp.strip()
        striped_temp = float(striped_temp)
        lista.append(striped_temp)

    return lista


def cria(linhas, colunas):
    return {'linhas': linhas, 'colunas': colunas, 'dados': {}}


#[[0,3],[1,2]]
def criaLst(matriz_lst):
    linhas = len(matriz_lst) #2
    colunas = len(matriz_lst[0]) #2
    dados = {} #{(0,1): 3, (1,0):1, (1,1):2}
    for i in range(linhas):
        for j in range(colunas):
            if matriz_lst[i][j] != 0: #Cast to int before
                dados[i,j] = matriz_lst[i][j]
    
    return {'linhas': linhas, 'colunas': colunas, 'dados': dados}


def carrega(nome_arquivo):
    #Tratar os \n e usar 'separa_pal'
    matriz_file = open(nome_arquivo, 'rt', encoding='utf8')
    linha_matriz = matriz_file.readline()

    matriz_lst = []

    while linha_matriz != "":
        matriz_lst.append(separa_pal(linha_matriz))
        linha_matriz = matriz_file.readline()
    
    matriz_file.close()

    return criaLst(matriz_lst)


def salva(tadMat, nome_arquivo):
    matriz_file = open(nome_arquivo, 'wt', encoding='utf8')

    linhas = tadMat['linhas']
    colunas = tadMat['colunas']

    linha_lst = []

    for l in range(linhas):
        for c in range(colunas):
            linha_lst.append(str(getElem(tadMat,l,c)))
        matriz_file.write(" ".join(linha_lst)+"\n")
        linha_lst.clear()

    matriz_file.close()

    return tadMat

def destroi():
    return None


def getElem(tadMat, linha, coluna):
    chave = (linha,coluna)
    if linha < tadMat['linhas'] and coluna < tadMat['colunas']:
        if chave in tadMat['dados'].keys():
           return tadMat['dados'][chave]
        else:
            return 0
    else:
        return None


def setElem(tadMat, linha, coluna, valor):
    chave = (linha,coluna)
    if linha < tadMat['linhas'] and coluna < tadMat['colunas']:
        if chave in tadMat['dados'].keys():
            existente = tadMat['dados'][chave]
        else:
            existente = 0

        if valor == 0 and existente == 0: 
            return
        elif valor == 0 and existente != 0: 
            del tadMat['dados'][linha, coluna]
        elif valor != 0 and existente == 0: 
            tadMat['dados'][linha, coluna] = valor
        elif valor != 0 and existente != 0: 
            tadMat['dados'][linha, coluna] = valor
    else:
        return None


def subtracao(tadMatA, tadMatB):
    #User o getElem e o setElem vai facilitar
    linhasA = tadMatA['linhas']
    colunasA = tadMatA['colunas']
    if (linhasA == tadMatB['linhas']) and (colunasA == tadMatB['colunas']):
        tadMatC = cria(linhasA, colunasA)
        for l in range(linhasA):
            for c in range(colunasA):
                setElem(tadMatC,l,c,getElem(tadMatA,l,c) - getElem(tadMatB,l,c))

        return tadMatC
    else:
        return None


def soma(tadMatA, tadMatB):
    #User o getElem e o setElem vai facilitar
    linhasA = tadMatA['linhas']
    colunasA = tadMatA['colunas']
    if (linhasA == tadMatB['linhas']) and (colunasA == tadMatB['colunas']):
        tadMatC = cria(linhasA, colunasA)
        for l in range(linhasA):
            for c in range(colunasA):
                setElem(tadMatC,l,c,getElem(tadMatA,l,c) + getElem(tadMatB,l,c))

        return tadMatC
    else:
        return None


def vezesK(tadMat, k):
    linhas = tadMat['linhas']
    colunas = tadMat['colunas']
    for l in range(linhas):
        for c in range(colunas):
            setElem(tadMat,l,c,getElem(tadMat,l,c) * k)

    return tadMat


def multi(tadMatA, tadMatB):
    colunasA = tadMatA['colunas']
    linhasB = tadMatB['linhas']

    if colunasA == linhasB:
        linhasA = tadMatA['linhas']
        colunasB = tadMatB['colunas']

        tadMatC_lst = []
  
        for l in range(linhasA):
            tadMatC_lst.append([])
            for c in range(colunasB):
                tadMatC_lst[l].append(0)
                for k in range(colunasA):
                    tadMatC_lst[l][c] += getElem(tadMatA, l, k) * getElem(tadMatB, k, c)

        return criaLst(tadMatC_lst)
            
    else:
        return None


def clona(tadMat):
    linhas = tadMat['linhas']
    colunas = tadMat['colunas']
    dados = tadMat['dados']
    return {'linhas': linhas, 'colunas': colunas, 'dados': dados }


def quantLinhas(tadMat):
    return tadMat['linhas']


def quantColunas(tadMat):
    return tadMat['colunas']


def diagP(tadMat):
    diagP_lst = []
    linhas = tadMat['linhas']
    colunas = tadMat['colunas']
    if linhas == colunas:
        for l in range(linhas):
            for c in range(colunas):
                if l == c:
                    diagP_lst.append(getElem(tadMat,l,c))
        return diagP_lst
    else:
        return None


def diagS(tadMat):
    diagS_lst = []
    linhas = tadMat['linhas']
    colunas = tadMat['colunas']
    if linhas == colunas:
        for l in range(linhas):
            for c in range(colunas):
                if (colunas + 1) == (l + c):
                    diagS_lst.append(getElem(tadMat,l,c))
        return diagS_lst
    else:
        return None


def transposta(tadMat):
    linhas = tadMat['linhas']
    colunas = tadMat['colunas']
    dados = tadMat['dados']
    dados_t = {}
    for key in dados:
        dados_t[key[1],key[0]] = dados[key]
        
    tadMat['dados'] = dados_t
