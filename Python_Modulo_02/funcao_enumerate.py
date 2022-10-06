#a função enumerate pode ser usada para identificar a posição de um objeto em um conjunto (set)

carros = {'Gol', 'Celta', 'Palio',}

# a cada volta do laço for = indice(Nº)+1 e objeto(carro)+1
for indice, objeto in enumerate(carros):
    print(f'{indice} : {objeto}')