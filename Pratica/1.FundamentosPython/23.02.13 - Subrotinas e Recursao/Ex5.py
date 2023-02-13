import math

def entrada_inteiro_positivo():
    n = int(input("Insira um número inteiro positivo:"))
    while n < 1:
        n = int(input("Inválido. Insira um número inteiro positivo: "))
    return n

def e_perfeito (n):
    somaDivs = 0

    for i in range(1, n):
        if n % i == 0:
            somaDivs += i

    if n == somaDivs:
        return True
    else:
        return False

num = entrada_inteiro_positivo()

print("Os perfeitos entre 2 e esse número são: ")

for numero in range(2, num):
    if e_perfeito(numero) == True:
        print(numero)
