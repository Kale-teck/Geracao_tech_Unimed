nome = input('Informe seu nome: ')
idade = input('Informe a sua idade: ')

print(nome, idade, end=' ') #espaço e outro print na mesma linha
print(nome, idade, end='...\n') # 3 pontos e quebra de linha
print(nome, idade, sep='...\n') # 3 pontos e quebra de linha como separador