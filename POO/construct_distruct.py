#__init__ é um construtor e é usado sempre que criamos uma nova classe

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): #self foi definido por convenção
        self.cor = cor # self permite à classe chamar(acessar) seus próprios atributos e métodos
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

#o método __del__ é pouco usado em python pq o python tem um coletor de lixo
#que limpa a memória aautomaticamente

