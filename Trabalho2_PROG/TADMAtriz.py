def cria(linhas, colunas):
    return {'linhas': linhas, 'colunas': colunas, 'dados': {}}

#[[0,3],[1,2]]
def criaLst(matriz_lst):
    linhas = len(matriz_lst) #2
    colunas = len(matriz_lst[0]) #2
    dados = {} #{(0,1): 3, (1,0):1, (1,1):2}
    for i in range(linhas):
        for j in range(colunas):
            if matriz_lst[i][j] != 0:
                dados[i,j] = matriz_lst[i][j]
    
    return {'linhas': linhas, 'colunas': colunas, 'dados': dados}

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

#tadMatA = [[1,2], tadMatB = [[-1,3], tadMatC = [[ 7,7],
#           [3,4]]            [ 4,2]]            [13,17]]
def multi(tadMatA, tadMatB):
    colunasA = tadMatA['colunas']
    linhasB = tadMatB['linhas']

    if colunasA == linhasB:
        linhasA = tadMatA['linhas']
        colunasB = tadMatB['colunas']

        tadMatC = cria(linhasA, colunasB)
        
                
                
    else:
        return None
    
    return 0
