class Veiculo: #classe base(pai)

  def __init__(self, cor, placa, n_rodas):  #atributos
    self.cor = cor  #atributo
    self.placa = placa  #atributo
    self.n_rodas = n_rodas  #atributo

  def ligar_motor(self):
    print('Ligando motor')


class Motocicleta(Veiculo):
  pass


class Carro(Veiculo):
  pass


class Caminhao(Veiculo):
  pass

moto = Motocicleta('preta', 'abc-1234', 2)
carro = Carro('Prata', 'gcb-1523', '4')
moto.ligar_motor()

truck = Caminhao('Vermelho', 'gfd-8712', 8)
truck.ligar_motor()
