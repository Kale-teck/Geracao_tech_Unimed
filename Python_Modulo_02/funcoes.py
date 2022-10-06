# funções são blocos de códigos representados por um identificador e possuem entrada(argumentos) e saída(retorno)

#usar  funções = programação estruturadas

def mensagem():
    print('Hello, World!')
#se a variável for declarada, se na chamada não receber valor dará um erro!
def mensagem_2(nome): #nome = argumento
    print(f'Seja bem vindo {nome}')

def mensagem_3(nome = 'Anônimo'):
    print(f'Seja bem vindo {nome}!')

nome = input('Qual seu nome ? ')
mensagem_2(nome) #o valor também pode ser inserido direto como argumento
#Qual o seu nome? João
#seja bem vindo João !

print(mensagem_3()) #seja bem vindo anônimo ! (por padrão)
#porém se um argumento for passado para mensagem_3('exemplo') ele será aceito
