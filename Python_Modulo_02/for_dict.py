contatos = {
    "guilherme@gmail.com": { " nome " : " Guilherme " , " telefone " : " 3333-2221 " },
    "giovanna@gmail.com": { " nome " : " Giovanna " , " telefone " : " 3443-2121 " } ,
    "chappie@gmail.com": { " nome " : " Chappie " , " telefone " : " 3344-9871 " } ,
    "melaine@gmail.com": { " nome " : " Melaine " , " telefone " : " 3333-7766 ", 'extra': {'carro':'Gol', 'Classe':'Hatch'} },}

#esse for itera por contatos atribuindo chave e valor para uma varável de qualquer nome

for chave,valor in contatos.items(): #função items casa bem com dict
    print(chave, valor)

print(contatos.keys()) #retorna as chaves contidas no dict

#se você quer remover um objeto dict mas não tem certeza da sua existencia utilize o metodo .pop()
teste_de_pop = contatos["melaine@gmail.com"]['extra'].pop('carro', 'não conseguiu') #retornou Gol
print(teste_de_pop)

print('carro' in contatos["melaine@gmail.com"]['extra']) #retornou True