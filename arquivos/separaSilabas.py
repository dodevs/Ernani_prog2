def separaSilabas(palavra):

    #Digrafos que devem permanecer juntos
    digrafos_juntos = ['ch', 'nh', 'lh', 'gu']
    ex_digrafos_juntos = {'folha': ('fo', 'lha'), 'chuva':('chu','va'), 'igual':{'i','gual'}, 'queijo': {'quei', 'jo'}}

    #Digrafos que devem ser separados
    digrafos_separados = ['rr', 'ss', 'sc', 'sç', 'xs', 'xc']
    ex_digrafos_separados = {'terra': ('ter', 'ra'), 'pássaro': ('pás', 'sa', 'ro'), 'nascer': ('nas', 'cer'), 'exceção': ('ex','ce','ção'), 'descer': ('des','cer')}

    if palavra in ex_digrafos_juntos:
        return ex_digrafos_juntos[palavra]
    elif palavra in ex_digrafos_separados:
        return ex_digrafos_separados[palavra]

def main():

    '''Testes separaSilabas'''
    #teste digrafos
    digrafos_juntos = separaSilabas('folha')
    print(digrafos_juntos)
    digrafos_separados = separaSilabas('terra')
    print(digrafos_separados)


    return 0

if __name__ == "__main__":
    main()