#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main3aAVALmat.py
#
#  Ifes Campus Serra - CIN - BSI
#  
#  Copyright 2018 <NOME DO ALUNO AQUI> <E-MAIL DO ALUNO AQUI>
#  
# ############################################################

import tadmatriz as tadm


def separa_pal(line):
    temp = ''
    lista = []
    for i in range(len(line)):
        if line[i] != ',':
            temp += line[i]
        elif len(temp) > 0:
            striped_temp = temp.strip()
            lista.append(striped_temp)
            temp = ''
    if len(temp) > 0:
        striped_temp = temp.strip()
        lista.append(striped_temp)

    return lista


def main(args):
    #####################################################################################
    ## 
    ## IMPLEMENTE AQUI A LÓGICA RESPONSÁVEL PELO PROCESSAMENTO DO ARQUIVO bdaritmat.csv,
    ## REPRESENTADA NA FIGURA 1 DA QUESTÃO 1.
    ## 
    #####################################################################################

    bdmat = open('bdaritmat.csv', 'rt', encoding="utf8")
    linha_op = bdmat.readline()
    while linha_op != '':
        operacao = separa_pal(linha_op)
        
        linha_op = bdmat.readline()
    
    return 0
## fim main ..

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
