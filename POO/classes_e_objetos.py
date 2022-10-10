class Cachorro: #classe chamada cachorro
    def __init__(self, nome, cor, acordado=True): # padrão (acordado)
        self.nome = nome #caracteristicas
        self.cor = cor #caracteristicas
        self.acordado = acordado #caracteristicas

    def latir(self): #comportamento
        print('Auau')


    def dormir(self): #comportamento (define acordado para False)
        self.acordado = False
        print('zzzzzzzz...')

#USANDO A CLASSE EM UM OBJETO

cao_1 = Cachorro('Rodolfo', 'caramelo')
cao_2 = Cachorro('Nega', 'Preta')

cao_1.dormir()

print(f'Oi eu sou {cao_1.nome} e minha cor é {cao_1.cor}')