#polimorfismo é a capacidade de um mesmo objeto possuir "comportamentos" diferentes
class Ave:
    def voar(self): #nesse caso voar é polimórfico, pois ao longo do código muda-se o comportamento do mesmo
        print('Voando...')
class Pardal(Ave):
    def voar(self):
        super().voar() #trás os atributos da sueprclasse(mãe) Ave para a subclasse(filha) Pardal
class Avestruz(Ave):
    def voar(self):
        print('Avestruz não voa...') #ao invés de importar print... define seu próprio

def plano_voo(obj): #cria a função com um objeto como argumento
    obj.voar() #perceba que o mesmo objeto tem dois comportamentos (polimorfismo)

p1 = Pardal()
p2 = Avestruz()

plano_voo(p1) #voando
plano_voo(p2) #avestruz não pode voar