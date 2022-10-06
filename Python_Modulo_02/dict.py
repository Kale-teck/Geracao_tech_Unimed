from ast import dump


pessoa = {'nome':'Kalebe', 'idade':23}
#chave = nome e valor = Kalebe

#as chaves são imutáveis porém os valores não

pessoa['telefone'] = '3381-7777'

print(pessoa['nome'])

pessoa['nome'] = 'Maria' #sobrescreve Nome
print(pessoa)

#dict's suportam objetos multidimensionais como matrizes ou bds

contatos = {
    "guilherme@gmail.com": { " nome " : " Guilherme " , " telefone " : " 3333-2221 " },
    "giovanna@gmail.com": { " nome " : " Giovanna " , " telefone " : " 3443-2121 " } ,
    "chappie@gmail.com": { " nome " : " Chappie " , " telefone " : " 3344-9871 " } ,
    "melaine@gmail.com": { " nome " : " Melaine " , " telefone " : " 3333-7766 ", 'extra': {'carro':'Gol', 'Classe':'Hatch'} },}
#nessa última linha adicionamos um dicionário a este dicionário

print(contatos["giovanna@gmail.com"][" telefone "]) # " 3443-2121 "

#acessando
#pode-se navegar palo dicio como em um banco de dados
teste = contatos["melaine@gmail.com"]['extra']['carro']

print(teste)

dump(dict(contatos))

