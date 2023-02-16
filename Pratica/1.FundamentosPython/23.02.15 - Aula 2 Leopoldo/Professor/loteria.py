import random, sys

qtde, min, max = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

def numeros_loteria(qtde:int, min:int, max:int):
    numeros = []
    if qtde>0 and max>min and qtde <= (max-min):
        for i in range(0,qtde):
            numero = random.randrange(min, max)
            while numero in numeros:
                numero = random.randrange(min,max)
            numeros.append(numero)
    numeros.sort()
    return numeros

# numeros_loteria(int('1'),int('1'),int('10'))
# for numero in numeros_loteria(12,1,11):
#     print(numero)
print(numeros_loteria(qtde,min,max))

# print(list(range(0,-12)))