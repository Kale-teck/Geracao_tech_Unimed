class Foo:
    def __init__(self, x=None):
         self._x = x
    
    @property # faz x retornar um valor
    def x(self):
        return self._x or 0 #se x tiver algum valor return valor de x, se não retorna 0
    
    @x.setter # permite alterar x com =
    def x(self, value):
        self._x += value
    
    @x.deleter # limpa x com del e atribui 0
    def x(self):
        self._x = 0

foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)
