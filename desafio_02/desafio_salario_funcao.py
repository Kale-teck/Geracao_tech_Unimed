#aqui um exemplo da função que fiz em separado sem os if's apenas para teste
def reajustando(salario, porcentagem):
    reajuste = (porcentagem * salario) / 100
    return print(f'Novo salario {reajuste+salario:,.2f} \nReajuste ganho: {reajuste:,.2f} \nEm percentual: {porcentagem} %')

reajustando(100, 17)