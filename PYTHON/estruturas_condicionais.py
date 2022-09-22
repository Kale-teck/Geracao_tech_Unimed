MAIOR_IDADE = 18
IDADE_ESPECIAL = 60

idade = int(input('Informe sua idade: '))

if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar CNH.')
elif idade > IDADE_ESPECIAL:
    print('Aulas práticas opcionais')
else:
    print('Menor de idade, Não pode emitir CNH')