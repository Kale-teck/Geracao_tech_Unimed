#método apend

lista = []

lista.append(1)
lista.append('olá!')

print(lista)

#método clear limpa a lista

lista.clear()

print(lista)

#método copy faz uma cópia da lisa original
lista = [1, 'Python', [40, 30, 20]]

l2 = lista.copy()

print(id(l2), id(lista)) #veja que l2 e lista estão em locais  diferentes e podem ser trabalhadas sem que uma afete a outra

#método count() conta quantos objetos há em uma lista

print(lista.count('Python')) #retorna quantas vezes o objeto argumentado aparece na lista