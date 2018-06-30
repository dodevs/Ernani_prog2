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

def ordena_quick(lista_dados, coluna):
    from random import randint
    left = []
    right = []

    pivo = randint(1,len(lista_dados)-1)

    if lista_dados:
        #left = [x for x in lista_dados if x < lista_dados[0]]
        for x in lista_dados:
            if x[coluna] < lista_dados[pivo][coluna]:
                left.append(x)

        #right = [x for x in lista_dados if x > lista_dados[0]]
        for x in lista_dados:
            if x[coluna] > lista_dados[pivo][coluna]:
                right.append(x)

        if len(left) > 1:
                left = ordena_quick(left,coluna)
        if len(right) > 1:
                right = ordena_quick(right,coluna)

        return left + [lista_dados[0]] * lista_dados.count(lista_dados[0]) + right
    return []

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
    #lista_arquivos = particiona('Teste.csv', 2)
    
    for arquivo in lista_arquivos:
        table_list = table_to_list(arquivo)
        ordened_table_list = ordena_quick(table_list,2)
        list_to_table(arquivo, ordened_table_list)

if __name__ == "__main__":
    main()