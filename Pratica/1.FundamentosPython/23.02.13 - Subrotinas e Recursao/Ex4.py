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

print("Os primos entre 2 e esse número são: ")

for numero in range(2, num):
    if e_primo(numero) == True:
        print(numero)
