#método union

conjunto_a = {1,2,3}
conjunto_b = {3,4,2}
#exibe {1,2,3,4}
print(conjunto_a.union(conjunto_b)) #retorna o conjunto sem repetiçoes a+b
print(conjunto_a.intersection(conjunto_b)) #retorna o objeto que se repete em a e b
print(conjunto_a.difference(conjunto_b)) #retorna o objeto que não se repete de a para b
print(conjunto_b.difference(conjunto_a)) #retorna o objeto que não se repete de b para a

#.simetric_difference retorna os objetos mais distantes entre si

#.issubset() retorna se a é subconjunto de b (true and false)

#.isdisjoint() testa se a não está contido em b (true and false)

#.add()

conjunto_a.add(6)
print(conjunto_a) # 6 foi adicionado pois não existia, caso contrário seria ignorado pelo python

#.clear() limpa o conjunto
#.copy() faz uma cópia do comjunto
#.discard() discarta o valor especificado

print(conjunto_a.discard(6))
print(conjunto_a) # descartou o 6 adicionado anteriormente

#.pop() remove o último valor da lista/tupla/conjunto
#.remove() remove o valor especificado (porém dá erro se o valor não existir mais) != .discard()

#.len() retorna o tamanho do conjunto(set)/var/let/tuple/list