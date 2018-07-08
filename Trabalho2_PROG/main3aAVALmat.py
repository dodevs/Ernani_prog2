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

def operacao_matriz(tadMat, operacao, alvo):
    if not alvo.isalpha() and operacao == '*':
        tadm.vezesK(tadMat, float(alvo))
        return tadMat
    else:
        tadMatB = tadm.carrega('./bdmatrizes/{}.txt'.format(alvo))
        if operacao == '*':
            return tadm.multi(tadMat, tadMatB)
        elif operacao == '+':
            return tadm.soma(tadMat, tadMatB)
        elif operacao == '-':
            return tadm.subtracao(tadMat, tadMatB)


def print_diag(tadMat_diag, _str):
    print("\n\nDiagonal %s da matriz :" % _str, end="\n\n")
    for elem in tadMat_diag:
        print("%.1f" % elem, end=" "*2)


def main(args):
    #####################################################################################
    ## 
    ## IMPLEMENTE AQUI A LÓGICA RESPONSÁVEL PELO PROCESSAMENTO DO ARQUIVO bdaritmat.csv,
    ## REPRESENTADA NA FIGURA 1 DA QUESTÃO 1.
    ## 
    #####################################################################################

    bdmat = open('bdaritmat.csv', 'rt', encoding="utf8")
    linha_op = bdmat.readline()
    tadMat = None

    while linha_op != '':
        operacao = separa_pal(linha_op)
        if len(operacao) == 1:
            if operacao[0] == 't' and tadMat != None:
                tadm.transposta(tadMat)
            else:
                tadMat = tadm.carrega('./bdmatrizes/{}.txt'.format(operacao[0]))
        else:
            tadMat = operacao_matriz(tadMat, operacao[0], operacao[1])
        linha_op = bdmat.readline()

    bdmat.close()
    tadm.salva(tadMat, "Q1.txt")

    tadMat_diagP = tadm.diagP(tadMat)
    tadMat_diagS = tadm.diagS(tadMat)

    print_diag(tadMat_diagP, "principal")
    print_diag(tadMat_diagS, "secundária")

    return 0
## fim main ..

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
