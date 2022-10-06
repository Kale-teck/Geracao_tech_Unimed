carros = ['Gol', 'Celta', 'Palio']

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros): #indice=contador carro=iteravel
    print(f'{indice+1}: {carro}') #contador+1: iteravel
