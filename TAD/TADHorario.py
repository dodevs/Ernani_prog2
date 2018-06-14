'''Tipos abstratos de dados

* É composto por uma estrutura de dados e um interface
** A interface é por onde manipulamos a estrutura

'''

class Horario():
    
    def __init__(self,h,m,s):
        self.segundos = s
        self.minutos = m
        self.horas = h

def cria(h,m,s):
    return [h,m,s]

def getHoras():
    return 0

def getMinutos():
    return 0

def getSegundos():
    return 0

def emSegundos():
    return 0

def somaHora(TADHorario0,TADHorario1):
    return 0