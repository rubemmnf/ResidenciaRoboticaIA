#Descriptors
# __set__
# __get__

class Constante(object):
    def __init__(self,valor):
        self.valor = valor
    def __set__(self, *_):
        pass
    def __get__(self, *_):
        return self.valor

class X:
    c = Constante(13)

if __name__=='__main__':
    
    x = X()
    print(x.c)
    x.c = 42
    print(x.c)
    # c = Constante(12)
    # print(c.valor)#C.__get__(self,...)
    # c.valor = 14
    # c.teste = 15
    # print(c.teste)
    # print(c.valor)