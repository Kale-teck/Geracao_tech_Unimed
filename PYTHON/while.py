opcao = -1

while opcao != 0: #enquanto opção for diferente de zero
    opcao = int(input('[1] sacar\n [2] Extrato\n [0] Sair\n: '))

    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Extrato...')
else: #inverso do while: se opção for igual a zero, exibe esta mensagem e sai
    print('Obrigado por usar nosso sistema, até logo! ')
#pode-se usar beak: para sair de um loop em determinada condição
#continue: pula a vez atual do loop