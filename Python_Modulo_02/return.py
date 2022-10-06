# return = 'none' se nenhum valor for informado

def calcular_total(numeros):
    return sum(numeros)

print(calcular_total([10, 20, 30])) #imprime 60

def antecessor_antecessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(antecessor_antecessor(10)) #imprime (9, 11)

