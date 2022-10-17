# não podea acessar ou modificar o estado da classe

#usado para criar funções utilitárias

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

p = Pessoa('Guilherme', 28)
print(p.nome, p.idade)