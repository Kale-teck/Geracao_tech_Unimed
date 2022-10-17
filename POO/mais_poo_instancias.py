class Estudante: #superclass
    escola = 'IF' #string default = 'IF'
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self) -> str:
        return f'{self.nome} mat({self.matricula}) - {self.escola} \n'

kal = Estudante('Kalebe', 123456789)
rob = Estudante('Robert', 98765432)

print(kal, rob)