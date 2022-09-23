valores = input().split()

total_hotdog = int(valores[0])
total_participante = int(valores[1])

if total_hotdog >= 1 and total_participante <= 1000:
    media_hotdog = float(total_hotdog / total_participante)

print(f'{media_hotdog:.2f}')