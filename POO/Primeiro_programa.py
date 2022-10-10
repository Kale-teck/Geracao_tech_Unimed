#bicicletaria
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): #self foi definido por convenção
        self.cor = cor # self permite à classe chamar(acessar) seus próprios atributos e métodos
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print('Plim Plim...')
    
    def parar(self):
        print('Parando bicicleta')
        print('Bicicleta parada!')
    
    def correr(self):
        print('Vruuummm!!!')
    
    def __str__(self):
        return f'{self.__class__.__name__}' #retorna o nome da classe

b1 = Bicicleta('vermelha', 'caloi', 2022, 600) #criando um objeto da classe Bicicleta

b1.buzinar() #chamando métodos (métodos são funções pertencentes a uma classe)
b1.correr()
b1.parar()
print(b1.__str__()) #acessando método que retorna o nome da classe a que o objeto pertence

print(b1.cor, b1.modelo, b1.ano, b1.valor) #acessando os atributos
