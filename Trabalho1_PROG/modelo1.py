arq_entrada1 = open(lista_arquivos_partes[0],'rt')
    arq_saida = open(nome_arquivo_total,'wt')
    
    for i in range(1, len(lista_arquivos_partes)):
        if arq_saida.closed:
            arq_saida = open(nome_arquivo_total,'wt')

        arq_entrada2 = open(lista_arquivos_partes[i],'rt')

        linha_arq1 = arq_entrada1.readline()
        linha_arq2 = arq_entrada2.readline()

        while linha_arq1 != '' or linha_arq2 != '':
            cmp_arq1 = linha_arq1.split(';')
            cmp_arq2 = linha_arq2.split(';')
            if len(cmp_arq1) > 1 and len(cmp_arq2) > 1: 
                if cmp_arq1[2] < cmp_arq2[2]:
                    arq_saida.write(linha_arq1)
                    linha_arq1 = arq_entrada1.readline()
                elif cmp_arq1[2] == cmp_arq2[2]:
                    if cmp_arq1[3] < cmp_arq2[3]:
                        arq_saida.write(linha_arq1)
                        linha_arq1 = arq_entrada1.readline()
                    elif cmp_arq1[3] == cmp_arq2[3]:
                        if cmp_arq1[1] < cmp_arq2[1]:
                            arq_saida.write(linha_arq1)
                            linha_arq1 = arq_entrada1.readline()
                        else:
                            arq_saida.write(linha_arq2)
                            linha_arq2 = arq_entrada2.readline() 
                    else:
                        arq_saida.write(linha_arq2)
                        linha_arq2 = arq_entrada2.readline()
                else:
                    arq_saida.write(linha_arq2)
                    linha_arq2 = arq_entrada2.readline()

            elif len(cmp_arq1) == 1:
                arq_saida.write(linha_arq2)
                linha_arq2 = arq_entrada2.readline()
            else:
                arq_saida.write(linha_arq1)
                linha_arq1 = arq_entrada1.readline()

        arq_entrada1.close()
        arq_entrada2.close()

        arq_entrada1 = open(nome_arquivo_total, 'rt')

        arq_saida.close()

    arq_entrada1.close()

    [ remove(arquivo) for arquivo in lista_arquivos_partes]
    
    return nome_arquivo_total