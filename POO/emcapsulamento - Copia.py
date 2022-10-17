#consiste em restringir o acesso à manipulação externas à classe

#Público: edição global
#Privado: edição local

class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo #o _ deveria restringir o acesso
    
    def depositar(self, valor):
        pass #o bloco de alteração de _saldo de ser feito através de funções internas
    
    def sacar(self, valor):
        pass  #o bloco de alteração de _saldo de ser feito através de funções internas
    
    def mostrar_saldo(self):
        return self._saldo # um exemplo de método que acessa _saldo

conta = Conta(100) #o interpretador permite essa alteração pois Python é dinâmicamente tipata e naturalmente não faz essa restrição de acesso
print(conta._saldo) # 100 (forma errada)
print(conta.mostrar_saldo()) # 100 (forma correta)
#por convensão variáveis que começam com underline não devem ser alteradas diretamente
#elas devem possuir métodos(funções) dentro de suas respectivas classes para serem usadas