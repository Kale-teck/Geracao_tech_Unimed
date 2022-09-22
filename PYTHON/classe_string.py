curso = 'pyThon'

print(curso.upper()) # maiúsculas
print(curso.lower()) # minúsculas
print(curso.title()) # Título

texto = '      Olá, Mundo!   '
print(texto.strip()) # remove todos espaços em branco

#junções e centralização

print(curso.center(20, '#')) # centraliza o objeto e adiciona caracteres
print(','.join(curso)) # percorre curso e adiciona ',' a cada elemento

#fatiamento de string
#tecnica usada para retornar substrings

nome = 'João Maria da Silva'

print(nome[0]) #índice zero
print(nome[:9]) # até o índice nove
print(nome[9:]) # do 10 ao final
print(nome[5:10]) # começo e fim definidos (substring)
print(nome[5:15:2]) #start:stop:step (começo, fim e passo)
print(nome[::-1]) # retorna a string de trás pra frente

#string multilinha

texto2 = f'''
    Olá meu nome é {nome}
    Sejam bem vindos ! '''

print(texto2)