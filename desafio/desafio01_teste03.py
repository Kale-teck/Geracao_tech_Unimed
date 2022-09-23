valores = input().split()

tempo_viagem = int(valores[0])
velocidade_media = int(valores[1])

litros_viagem = tempo_viagem * velocidade_media / 12

print(f'{litros_viagem:.3f}')