#Versão anterior

'''num = int(input("Insira um número inteiro positivo:"))
somaDivs = 0

while (num <= 0):
    num = int(input("Inválido. Insira um número inteiro positivo:"))

for i in range(1, num):
    if num % i == 0:
        somaDivs += i

if num == somaDivs:
    print("É perfeito")
else:
    print("Não é perfeito")'''

# Versão com subrotinas

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

if e_perfeito(num) == True:
    print("É perfeito")
else:
    print("Não é perfeito")