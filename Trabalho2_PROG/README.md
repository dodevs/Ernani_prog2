# 3ª Avaliação

## TAD Matriz 

* Nao armazenar zeros

#### Funções essenciais:
> - [x] cria
>   * cria()
>   * criaLst()
>   * carrega()
> - [x] soma
> - [x] multiplica
> - [x] vezesK
> - [x] clona
> - [x] diagP
> - [x] diagS
> - [x] quantLinhas
> - [x] quantColunas
> - [x] transposta
> - [ ] toString [Matriz bonita]
> - [x] salva

#### Exemplos:
```python
m = TADMat.cria(5,3)
return [5,3, {}]
return {'linhas':5, 'colunas':3, 'dados': {}}
```

```python
m = TADCriaLST([[0,2],[2,0]])
return [2,2,{ (0,1): 2, (1,0): 2}]
return {'linhas':2, 'colunas':2, 'dados':{(0,1):2, (1,0):2}}
```

```python
TADMat.setElem(m,1,2,0) # matriz, linha, coluna, elemento
```

```python
if novo == 0 and existente == 0: pass
if novo == 0 and existente != 0: del element
if novo != 0 and existente == 0: dados[1][2] = novo
if novo != 0 and existente != 0: dados[1][2] = novo
```

## TAD Polinomio

#### Funções essenciais:

> cria(str), soma, multiplica, toString

#### Exemplos:

```python
TADPoli.inic("25x4-17x2-47")
return {4:25, 2:-17, 0:-47}
```