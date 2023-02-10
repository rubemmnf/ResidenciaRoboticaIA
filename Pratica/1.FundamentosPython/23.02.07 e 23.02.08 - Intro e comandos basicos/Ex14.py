num1 = int(input("Insira o primeiro número inteiro positivo: "))
while num1 < 1:
    print("Inválido. Insira um número inteiro positivo: ")

num2 = int(input("Insira o segundo número inteiro positivo: "))
while num2 < 1:
    print("Inválido. Insira um número inteiro positivo: ")

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

print(mmc)