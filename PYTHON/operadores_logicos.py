saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(saldo >= saque and saque <= limite) #operador E
print(saldo >= saque or saque <= limite) #operador OU

not 1000 > 1500 #operador de negação retorna true pois 1000 não é maior que 1500

contatos_emergencia = []

not contatos_emergencia #retorna true pois cont... não possui nada

#parênsteses podem ser usados em operações lógicas para criar operções compostas ou alterar a ordem de precedência

comparacao1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
comparacao2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

#não é aconselhavél criar linhas de comparação muito extensas pois ficam pouco legivéis
#quebre em casos e atribua-os à variáveis

print(comparacao1) #retorna true
print(comparacao2) #retorna true