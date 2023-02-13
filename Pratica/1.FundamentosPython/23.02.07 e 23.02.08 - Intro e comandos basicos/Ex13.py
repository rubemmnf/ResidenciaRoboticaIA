num1 = int(input("Insira o primeiro número inteiro positivo: "))
while num1 < 1:
    num1 = int(input("Inválido. Insira um número inteiro positivo: "))

num2 = int(input("Insira o primeiro número inteiro positivo: "))
while num2 < 1:
    num2 = int(input("Inválido. Insira um número inteiro positivo: "))


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

print(mdc)

#Andar no sentido contrário só precisa achar um, desta forma, fazer com while