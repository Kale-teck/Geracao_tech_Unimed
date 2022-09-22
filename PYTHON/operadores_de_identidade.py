#são operadores usados para comparar se os dois valores objetos testados ocupam a mesma posição na memória

curso = 'Curso de Python'
nome_curso = curso
saldo, limite = 200, 200

id = curso is nome_curso #comapara se as duas variavéis estão no mesmo lugar da memória
print(id)

not_id = curso is not nome_curso #testa se as duas variavéis não estão no mesmo lugar da memória
print(not_id)

print(saldo is limite)
