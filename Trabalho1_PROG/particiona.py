import csv_tool

def particiona(nome_arquivo, partes):
    from os.path import getsize
    arquivo_path = 'Trabalho1_PROG/'+nome_arquivo
    arquivo_len_total = getsize(arquivo_path)//partes
    arquivo_len_resto = getsize(arquivo_path)%partes
    arquivo = open(arquivo_path)

    arquivoN_len_parcial = 0
    count = 0

    arquivo_linha = arquivo.readline()

    while arquivo_linha != '':
        if arquivoN_len_parcial <= arquivo_len_total:
            arquivoN = open('{}_{:03d}.csv'.format(arquivo_path.split('.')[0], count),'at')
            arquivoN.write(arquivo_linha)
            arquivoN_len_parcial += len(arquivo_linha)
            arquivo_linha = arquivo.readline()
        else:
            arquivoN.close()
            count += 1
            arquivoN_len_parcial = 0
    

def main():
    #particiona('Planilhas_Enem_2015_download.csv', 2)
    particiona('Teste.csv', 2)

if __name__ == "__main__":
    main()