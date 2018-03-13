#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  separaPal.py
#  
#  Autor: Douglas Silva <alunoifes@ifesubu-vb>
#  Criado em: 13/03/18 10:16:52
#  Usuário: IFES-Serra (BSI, Tecnicos de Informática)
#  Descrição: <resumo da tarefa que o programa realiza.>
#  
#  Versão inicial: 1.0
#  Ambiente: Geany v1.27 GNU GENERAL PUBLIC LICENSE
#  Sistema: Ubuntu 64b LTS
#  ----------------------------------------------------------------

def onList(lista, string):
    for i in range(len(lista)):
        if lista[i][0] == string:
            return True
    
    return False

def contaPal(lstPalavras):
    contador = 0
    tabelaFreq = []
    for i in range(len(lstPalavras)): #i = 1
        if not onList(tabelaFreq, lstPalavras[i]): #[], 'Oe'
            for j in range(i,len(lstPalavras)): 
                if lstPalavras[i] == lstPalavras[j]:
                    contador += 1
        
            tabelaFreq.append((lstPalavras[i], contador))
        contador = 0
        
    return tabelaFreq

def separaPal(text):
    strBuffer = ""
    lstPalavras = []
    
    for i in range(len(text)):
        #Se o caractere for 0-9 ou a-z
        if text[i].isalnum():
            strBuffer += text[i] #Adiciona no buffer para formar palavra
        else:
            #Se o strBuffer formado for maior que 0
            if len(strBuffer) > 0:
                if text[i] == '-':
                    #Se o ultimo caractere do strBuffer nao for um hifen
                    if strBuffer[-1] != '-':
                        strBuffer += text[i] #Entao é adicionado o hifen ao buffer
                    else: #Se for..
                        lstPalavras.append(strBuffer[:-1]) #Entao adiciona somente a palavra sem o hifen a lista
                        strBuffer = ''
                else:
                    lstPalavras.append(strBuffer)
                    strBuffer = ''
    if len(strBuffer) > 0:
        lstPalavras.append(strBuffer)
    
    return lstPalavras
            

def main(args):
    palavras = separaPal("Oe Oe tudo tudo bem tudo bem")
    print(contaPal(palavras))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
