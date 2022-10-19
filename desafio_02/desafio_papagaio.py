pernas = {'esquerda':'ingles', 'direita':'frances', 'nenhuma':'portugues', 'ambas':'caiu'}
perna_vez = 'nenhuma' # define perna_vez para True para entrar no while
x = 1
while perna_vez in pernas: 
    perna_vez = input()
    perna_vez = perna_vez.lower() #caixa baixa para evitar erros
    perna_vez = perna_vez.strip() #remove espaços no começo e no fim para evitar erros
    print(pernas[perna_vez])
    x += 1
    if x == 5:
        break