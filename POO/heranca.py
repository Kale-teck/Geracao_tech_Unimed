#herança é a capacidade da classe filha herdar caracteristicas da classe pai
#se a classe B herda características da classe A, então os filhos de B também herdam características de A

#exemplos do conceito

class A: #classe A não herda nada de ninguém
  pass #método pass representa um bloco nulo(em branco)

class B(A): # trad: cria classe B herdando de A
  pass  #bloco nulo (função vazia)

#HERANÇA MÚLTIPLA: quando uma classe filha herda características de várias classes pais

#exemplos

class C:
  pass

class D(A, C): # classe D herda de A e C (possui 2 pais)
  pass

print('Classes criadas')