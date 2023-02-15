import random

def numeros_loteria(qtde:int, min:int, max:int):
    lista = []
    
    if qtde > 0 and max > min and qtde <= max - min + 1:
        for num in range(qtde):
            termo = random.randint(min, max)
            while termo in lista:
                termo = random.randint(min, max)
            lista.append(termo)

    return lista

# for numero in numeros_loteria(6,1,60):
#     print(numero)
print(numeros_loteria(11,1,11))