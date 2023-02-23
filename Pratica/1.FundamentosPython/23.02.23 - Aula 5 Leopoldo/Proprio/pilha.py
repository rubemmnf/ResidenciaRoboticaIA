#criar classe pilha com atributo de tamanho e método de inserção e remoção
class Pilha:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__topo = -1
        self.__valores = []

    def push(self, valor):
        self.__topo += 1
        self.__valores.append(valor)
        return None

    def pop(self):
        try:
            self.__topo -= 1
            self.__valores.pop()
        except:
            raise "sem elementos para remover, tente adicionar mais (push) para continuar"

    def peek(self):
        try:
            return self.__valores[self.__topo]
        except:
            raise "passou da lista, remova elementos (pop) para continuar"

    def isEmpty(self):
        if self.__topo == -1:
            return True
        else:
            return False
        
pilhaTeste = Pilha(3)

print(pilhaTeste.isEmpty())
print(pilhaTeste.push(1))
print(pilhaTeste.isEmpty())
print(pilhaTeste.push(2))
print(pilhaTeste.peek())
print(pilhaTeste.push(3))
print(pilhaTeste.push(4))
