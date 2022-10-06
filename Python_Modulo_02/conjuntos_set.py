#classe set ou conjuntos, é uma função que não permite duplicar objetos (elementos)

from audioop import lin2adpcm


lista = [1,2,3,1,2,4,5]
print(set(lista)) # 1,2,3,4,5

print(set('abacaxi')) # não confiar na ordem da função set

linguagens = {'Python', 'Java', 'Python'} # chaves {} = "set()"

print(linguagens) # linguagens é um conjunto sem multiplicidade

#conjuntos não suportam indexação
#precisa-se converter o set para list

linguagens = list(linguagens) #após convertê-los para list
print(linguagens[1]) # aí sim pode-se selecionar um único índice

# também é possível percorrer um set com um for
linguagens = set('Python', 'Java')