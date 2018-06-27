import csv_tool

'''
    O codigo ta pegando além do tamanho previsto, corrigir isso
'''

def particiona(nome_arquivo, partes):
    from os.path import getsize
    arquivo_path = 'Trabalho1_PROG/'+nome_arquivo
    arquivo_len_total = getsize(arquivo_path)//partes
    arquivo = open(arquivo_path)

    arquivoN_len_parcial = 0
    linha_len = 1

    for i in range(partes):
        arquivoP = open('Trabalho1_PROG/{}_{:03d}.csv'.format(nome_arquivo.split('.')[0], i),'wt')
        while arquivoN_len_parcial < arquivo_len_total and linha_len > 0:
            buffer_arquivo_line = arquivo.readline()
            linha_len = arquivoP.write(buffer_arquivo_line)
            arquivoN_len_parcial += linha_len
        arquivoP.close()
        arquivoN_len_parcial = 0

def main():
    particiona('Planilhas_Enem_2015_download.csv', 200)
    #particiona('Teste.csv', 200)

if __name__ == "__main__":
    main()