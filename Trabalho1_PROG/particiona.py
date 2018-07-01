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
            if striped_temp.isdigit():
                striped_temp = int(striped_temp)
            listCells.append(striped_temp)
            temp = ''
    if len(temp) > 0:
        listCells.append(temp.strip())

    return listCells

def table_to_list(csv):
    table_list = list()
    table_file = open(csv, "rt")
    table_line = table_file.readline()

    while table_line != "":
        cells = split_cells(table_line)
        table_list.append(cells)

        table_line = table_file.readline()

    table_file.close()

    return table_list

def trocar(v, n, m):
    aux = v[n]
    v[n] = v[m]
    v[m] = aux

# É passado o vetor, a posicao de inicio e posicao final
def ordena_quick(v, start, end):
    if start < end: #condicao de parada
        q = particionar(v, start, end) # encontro o pivo
        ordena_quick(v, start, q-1) # pivotagem a esquerda (ordena os menores que o pivo)
        ordena_quick(v, q+1, end) # pivotagem a direita ( ... )

def particionar(v, start, end):
    pivo = v[start][1] # O pivo é o primeiro elemento da esquerda
    i = start # destino final do pivo
    j = start + 1 #contador para percorrer o restante do pivo
    
    while j <= end:
        if v[j][1] < pivo:
            i += 1 # detectou um elemento menor que o pivo, incrementa o i
            trocar(v, i, j)
        j += 1 #passa para o proximo elemento

    trocar(v, start, i)

    return i

def intercala(lista_arquivos_partes, nome_arquivo_total):
    pass

def particiona(nome_arquivo, partes):
    from os.path import getsize
    #from os import mkdir #Para criar uma pasta para os arquivos dividos

    lista_arquivos = []

    arquivo_len_total = getsize(nome_arquivo)//partes
    arquivo = open(nome_arquivo)

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

def main():
    
    lista_arquivos = particiona('Planilhas_Enem_2015_download.csv', 2)
    #lista_arquivos = particiona('Simple.csv', 2)
    
    for arquivo in lista_arquivos:
        table_list = table_to_list(arquivo)
        ordena_quick(table_list,0,len(table_list)-1)
        list_to_table(arquivo, table_list)

if __name__ == "__main__":
    main()