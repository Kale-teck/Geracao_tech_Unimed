#matrizes em Python possuem a mesma lógica de funcionamento que matrizes em linguagens C

matriz = [
    [1,'a',2],
    ['b',3,4],
    [6,5,'c']
]

print(matriz[0]) #retorna a primeira linha da Matriz
print(matriz[0][0]) #retorna a primeira linha e primeiro objeto dela
print(matriz[1][-1]) #retorna o último elemento da segunda linha
print(matriz[-1][-1]) #retorna a última linha e seu último valor

#fatiamento
#consiste em extrair um trecho da list e não apenas um índice isolado

lista = ['p','y','t','h','o','n']

print(lista[2:]) # thon = à partir do 3º elemento
print(lista[:2]) #py = até o 2º elemento
print(lista[1:3]) #yt = do 2º até o 3º
print(lista[0:3:2]) #pt = do 1º até o 3º objeto no passo 2 (step2)
print(lista[::]) #python = imprime toda list
print(lista[::-1]) #nohtyp = percorre a lista inversamente como em um for