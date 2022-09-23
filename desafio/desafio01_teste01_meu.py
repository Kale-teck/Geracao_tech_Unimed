distancia = int(input('Distância entre os Palatír : '))
diametro1 = int(input('Diâmetro do Palatír de Sauron : '))
diametro2 = int(input('Diâmetro do Palantír de Saruman : '))

if distancia > 0 and distancia < 10000:
    if diametro1 > 0 and diametro2 < 100:
        ICM = float(distancia / (diametro1+diametro2))
        print(f'aqui está o ICM dos Palatír de Sauron e Saruman : {ICM:.2f}')
    else:
        print('Valor de diâmetro incorreto detectado! ')   
else:
    print('Valor da distância incorreto! ')