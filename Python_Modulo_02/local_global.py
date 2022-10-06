salario = 2000 #salario é uma variavél global por ser declarada fora de uma fução

def salario_bonus(bonus):
    global salario #avisa pra função que salario é válida dentro da função
    salario += bonus
    return salario

print(salario_bonus(500))