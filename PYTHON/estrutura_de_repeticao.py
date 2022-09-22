texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

for letra in texto: #para letra em texto
    if letra.upper() in VOGAIS: #se letra está em vogais
        print(letra, end='') # end='' obriga os prints a estarem na mesma linha
else:
    print()

for numero in range(0, 51, 5): # começa em 0, para em 51 e pula a cada 5
    print(numero, end='  ')