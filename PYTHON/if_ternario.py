saldo = float(2000)
saque = float(input('Informe o valor do saque!'))

status = 'Sucesso' if saldo >= saque else 'Falha'

print(f'{status} ao realizar o saque!')