#Versão anterior

'''num1 = int(input("Insira o primeiro número inteiro positivo:"))
while num1 < 1:
    print("Inválido. Insira um número inteiro positivo: ")

num2 = int(input("Insira o segundo número inteiro:"))
while num2 < 1:
    print("Inválido. Insira um número inteiro positivo: ")

maior = 0
mdc = 1

if (num1 > num2):
    maior = num1
else:
    maior = num2

for i in range(1, maior+1, 1):
    if num1 % i == 0:
        if num2 % i == 0:
            mdc = i

print(mdc)'''

#Andar no sentido contrário só precisa achar um, desta forma, fazer com while

#Versão com subrotinas

def entrada_inteiro_positivo():
    n = int(input("Insira um número inteiro positivo:"))
    while n < 1:
        n = int(input("Inválido. Insira um número inteiro positivo: "))
    return n

def maior (n1, n2):
    maior = 0

    if (n1 > n2):
        maior = n1
    else:
        maior = n2

    return maior

def mdc(n1, n2):
    mdc = 0

    for i in range(1, maior(n1,n2)+1):
        if n1 % i == 0:
            if n2 % i == 0:
                mdc = i

    return mdc

num1 = entrada_inteiro_positivo()
num2 = entrada_inteiro_positivo() 

print (mdc(num1, num2))