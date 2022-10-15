class Animal(): #classe base(pai)
    def __init__(self, nro_patas): # atributos
        self.nro_patas = nro_patas # atributo(patas)
    
    def __str__(self):
        return f"{self.nro_patas}" #número de patas

class Mamifero(Animal): #Mamifero é um animal
    def __init__(self, nro_patas): # atributos
        super().__init__(nro_patas) # construtor (numero de patas)

class Ave(Animal): #Ave é um animal
    def __init__(self, nro_patas): # atributos
        super().__init__(nro_patas) # construtor (numero de patas)

class Cachorro(Mamifero): #cachorro pertence à mamifero, que é um animal
    pass

class Gato(Mamifero): #Gato pertence à mamifero, que é um animal
    pass

class Leao(Mamifero): #Leão é um mamifero, que é um animal
    pass

class Ornitorrinco(Mamifero, Ave): #O ornitorrinco é classificado pela ciência como ave e Mamífero ao mesmo tempo
    pass

bixano = Gato(4)
print(f'{bixano.nro_patas}') # exibe 4
print(bixano) # exibe 4 (forma mais simples por causa da função __str__ definida em animais)