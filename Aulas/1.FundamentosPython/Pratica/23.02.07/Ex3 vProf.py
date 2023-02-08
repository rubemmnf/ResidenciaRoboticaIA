n1 = int(input("Insira um número: "))
menor = 9999999999999999999999999999999999

for i in range(4):
    n1 = int(input("Insira um número: "))
    if n1 < menor:
        menor = n1

print("O menor deles é ", menor)