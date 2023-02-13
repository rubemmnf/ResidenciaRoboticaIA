#Versão anterior

'''num1 = int(input("Insira o primeiro número inteiro positivo: "))
while num1 < 1:
    num1 = int(input("Inválido. Insira um número inteiro positivo: "))

num2 = int(input("Insira o primeiro número inteiro positivo: "))
while num2 < 1:
    num2 = int(input("Inválido. Insira um número inteiro positivo: "))

menor = 0
mmc = num1 * num2
mmcInit = num1 * num2

if (num1 > num2):
    menor = num2
else:
    menor = num1

for i in range(mmcInit, menor-1, -1):
    if i % num1 == 0:
        if i % num2 == 0:
            mmc = i

print(mmc)'''

#Versão com subrotinas

def entrada_inteiro_positivo():
    n = int(input("Insira um número inteiro positivo:"))
    while n < 1:
        n = int(input("Inválido. Insira um número inteiro positivo: "))
    return n

def menor (n1, n2):
    menor = 0

    if (n1 > n2):
        menor = n2
    else:
        menor = n1

    return menor

def mmc(n1, n2):
    mmc = num1 * num2
    mmcInit = num1 * num2
    
    for i in range(mmcInit, menor(n1,n2)-1, -1):
        if i % n1 == 0:
            if i % n2 == 0:
                mmc = i

    return mmc

num1 = entrada_inteiro_positivo()
num2 = entrada_inteiro_positivo() 

print (mmc(num1, num2))