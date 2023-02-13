#Versão anterior
'''import math


num = int(input("Insira um número inteiro positivo:"))
raiz = math.sqrt(num)
d = 2

while d <= raiz and num % d != 0:
    d = d + 1

if d > raiz:
    print(num, 'é primo')
else:
    print(num, 'não é primo', d, 'é um divisor')'''

# Versão com subrotinas

import math

def entrada_inteiro_positivo():
    n = int(input("Insira um número inteiro positivo:"))
    while n < 1:
        n = int(input("Inválido. Insira um número inteiro positivo: "))
    return n

def e_primo(n):
    raiz = math.sqrt(num)
    d = 2

    while d <= raiz and n % d != 0:
        d = d + 1

    if d > raiz:
        return True
    else:
        return False

num = entrada_inteiro_positivo()

if e_primo(num) == True:
    print("É primo")
else:
    print("Não é primo")