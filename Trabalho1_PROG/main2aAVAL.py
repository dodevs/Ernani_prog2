#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main2aAVAL.py
#
#  Ifes Campus Serra - CIN - BSI
#  
#  Copyright 2018 <Douglas da Silva Sousa> <douglass.sousa@outlook.com.br>
#  
# ############################################################

def list_to_table(arquivo,table_list):
    newTableList = open(arquivo, 'wt')
    for line in table_list:
        line = ';'.join([str(cell) for cell in line])+'\n'
        newTableList.write(line)

    newTableList.close()

def split_cells(csv_line):
    temp = ''
    listCells = []
    for i in range(len(csv_line)):
        if csv_line[i] != ';':
            temp += csv_line[i]
        elif len(temp) > 0:
            striped_temp = temp.strip()
            if striped_temp.isnumeric():
                striped_temp = int(striped_temp)
            listCells.append(striped_temp)
            temp = ''
    if len(temp) > 0:
        listCells.append(temp.strip())

    return listCells

def table_to_list(csv):
    table_list = []
    table_file = open(csv, "rt")
    table_line = table_file.readline()

    while table_line != "":
        cells = split_cells(table_line)
        table_list.append(cells)

        table_line = table_file.readline()

    table_file.close()

    return table_list

def isNotVoid(files_line):
    i = False
    for line in files_line:
        if line != '':
            i = i or True
    return i

def menorChave(files_list, files_line_lst, splited_line_lst):
    menor = splited_line_lst[-1][3]
    i = 0
    while i < len(splited_line_lst)-1:
        for j in (2,3,1):
            if splited_line_lst[i][j] < menor:
                menor = i
            i += 1
        
    files_line_lst[i] = files_list[i].readline()
    return files_line_lst[i]


def intercala(lista_arquivos_partes, nome_arquivo_total):
    from os import remove

    arq_saida = open(nome_arquivo_total,'wt')

    files_list = [open(arquivo,'rt') for arquivo in lista_arquivos_partes]
    files_line_lst = [_file.readline() for _file in files_list]
    splited_line_lst = []

    while isNotVoid(files_line_lst):
        splited_line_lst = [line.split(';') for line in files_line_lst if line != '']
        arq_saida.write(menorChave(files_list,files_line_lst, splited_line_lst))

    [opened_file.close() for opened_file in files_list]
    arq_saida.close()

    return nome_arquivo_total


        


def trocar(v, n, m):
    aux = v[n]
    v[n] = v[m]
    v[m] = aux

# É passado o vetor, a posicao de inicio e posicao final
def ordena_quick(v, start, end):
    sys.setrecursionlimit(sys.getrecursionlimit() + 1)
    if start < end: #condicao de parada
        q = particionar(v, start, end) # encontro o pivo
        ordena_quick(v, start, q-1) # pivotagem a esquerda (ordena os menores que o pivo)
        ordena_quick(v, q+1, end) # pivotagem a direita ( ... )

def particionar(v, start, end):
    pivos = v[start][2], v[start][3], v[start][1] # O pivo é o primeiro elemento da esquerda
    i = start # destino final do pivo
    j = start + 1 #contador para percorrer o restante do pivo
    
    while j <= end:
        if v[j][2] < pivos[0]:
            i += 1 # detectou um elemento menor que o pivo, incrementa o i
            trocar(v, i, j)
        elif v[j][2] == pivos[0]:
            if v[j][3] < pivos[1]:
                i += 1
                trocar(v, i, j)
            elif v[j][3] == pivos[1]:
                if v[j][1] < pivos[2]:
                    i += 1
                    trocar(v, i, j)
        j += 1 #passa para o proximo elemento

    trocar(v, start, i)

    return i

def quick_partes(lst_nomes_arq_partes):    

    for arquivo in lst_nomes_arq_partes:
        table_list = table_to_list(arquivo)
        ordena_quick(table_list,0,len(table_list)-1)
        list_to_table(arquivo, table_list)
        
    return lst_nomes_arq_partes
# fim quick_partes

def particiona(nome_arquivo, partes):
    from os.path import getsize
    #from os import mkdir #Para criar uma pasta para os arquivos dividos

    lista_arquivos = []

    arquivo_len_total = getsize(nome_arquivo)//partes
    arquivo = open(nome_arquivo, 'rt')

    #Elimina os cabeçaçhos do arquivo
    '''
    arquivo.readline()
    arquivo.readline()
    arquivo.readline()
    '''

    #mkdir(nome_arquivo.split('.')[0], 0o755)  #Cria a pasta e define seu modo

    arquivoN_len_parcial = 0
    linha_len = 1

    for i in range(1, partes+1):
        arquivoP = open('{0}_{1:03d}.csv'.format(nome_arquivo.split('.')[0], i),'wt')
        while arquivoN_len_parcial < arquivo_len_total and linha_len > 0:
            buffer_arquivo_line = arquivo.readline()
            linha_len = arquivoP.write(buffer_arquivo_line)
            arquivoN_len_parcial += linha_len
        arquivoP.close()
        nome_arquivo_parte = '{0}_{1:03d}.csv'.format(nome_arquivo.split('.')[0], i)
        lista_arquivos.append(nome_arquivo_parte)
        arquivoN_len_parcial = 0
    
    return lista_arquivos

## ==> AS CHAMADAS DE TODAS AS FUNÇÕES ABAIXO SEGUEM A ASSINATURA DADA NA ESPECIFICAÇÃO.
def main(args):

    lst_partes = particiona("Teste.csv", 2)
    lst_partes = quick_partes(lst_partes)
    saida = intercala(lst_partes, "Teste2.csv")
    '''
    print("APLICAÇÃO PRINCIPAL DA 2a AVALIAÇÃO DE PROGRAMAÇÃO II:\n")
    print("Processando ..\n")
    lst_partes = particiona("Planilhas_Enem_2015_download.csv", 2)
    lst_partes = quick_partes(lst_partes)
    saida = intercala(lst_partes, "Planilhas_Enem_2015_sorted_2_partes.csv")
    print("Planilhas_Enem_2015_download.csv classificado em 2 partes em", saida)
    
    lst_partes = particiona("Planilhas_Enem_2015_download.csv", 3)
    lst_partes = quick_partes(lst_partes)
    saida = intercala(lst_partes, "Planilhas_Enem_2015_sorted_3_partes.csv")
    print("Planilhas_Enem_2015_download.csv classificado em 3 partes em", saida)
    
    lst_partes = particiona("Planilhas_Enem_2015_download.csv", 4)
    lst_partes = quick_partes(lst_partes)
    saida = intercala(lst_partes, "Planilhas_Enem_2015_sorted_4_partes.csv")
    print("Planilhas_Enem_2015_download.csv classificado em 4 partes em", saida)
    
    lst_partes = particiona("Planilhas_Enem_2015_download.csv", 5)
    lst_partes = quick_partes(lst_partes)
    saida = intercala(lst_partes, "Planilhas_Enem_2015_sorted_5_partes.csv")
    print("Planilhas_Enem_2015_download.csv classificado em 5 partes em", saida)
    
    lst_partes = particiona("Planilhas_Enem_2015_download.csv", 8)
    lst_partes = quick_partes(lst_partes)
    saida = intercala(lst_partes, "Planilhas_Enem_2015_sorted_8_partes.csv")
    print("Planilhas_Enem_2015_download.csv classificado em 8 partes em", saida)
    '''
    print("\n")
    print("concluido!")
    
    ## -----------------------------------------------------------------
    ## ==> OBS: NÃO É NECESSÁRIO, AO FINAL, APAGAR OS ARQUIVOS PARTES.
    ##          MAS SE APAGAR, O PROGRAMA FICARÁ MAIS 'PROFISSIONAL'
    ##          E MAIS BEM ACABADO.
    ## -----------------------------------------------------------------
    
    return 0
## fim main ..

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
