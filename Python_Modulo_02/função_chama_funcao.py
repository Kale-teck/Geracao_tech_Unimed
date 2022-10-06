# objetos de primeira classe são aqueles que podem ser chamados ou serem retornados
#funções tambem são objetos de primeira classe então podem ser chamados

def soma(a, b): 
    return a + b

def subtrai(a, b):
    return a - b

def exibe_resultado(a, b, funcao): #atribue a e b depois chama função
    resultado = funcao(a, b) #se a e b já foram definidos na chamada de exibe_resultado()
    print(f'O resultado da operação é = {resultado} ') # resultado == função(a, b) == soma(a, b)

exibe_resultado(10, 10, soma) #o resultado de 10 + 10 é 20
exibe_resultado(10, 10, subtrai) #o resultado de 10 - 10 é 0