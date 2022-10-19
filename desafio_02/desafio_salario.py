salario = float(input()) #entrada de salário

def reajustando(salario, porcentagem): # função que calcula
    reajuste = (porcentagem * salario) / 100 # cálculo de porcentagem
    novo_salario = reajuste+salario # salário final
    return print(f"Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {porcentagem} %") #inprime o que se pede na questão

if salario >= 0 and salario <= 600.00:
    porcentagem = 17
    reajustando(salario, porcentagem)

elif salario >= 600.01 and salario <= 900.00:
    porcentagem = 15
    reajustando(salario, porcentagem)

elif salario >= 900.01 and salario <= 1500.00:
    porcentagem = 12
    reajustando(salario, porcentagem)

elif salario >= 1500.01 and salario <= 2000.00:
    porcentagem = 10
    reajustando(salario, porcentagem)
else:
    porcentagem = 5
    reajustando(salario, porcentagem)

# TODO:  Calcule o salário do funcionário e print o novo salário, bem como o valor de reajuste ganho e o índice reajustado (em porcentagem)