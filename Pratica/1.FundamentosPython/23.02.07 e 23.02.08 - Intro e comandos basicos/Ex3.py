#entrada

num1 = float(input("Insira o primeiro número: \n"))
num2 = float(input("Insira o segundo número: \n"))
num3 = float(input("Insira o terceiro número: \n"))

#solução minha
menor = num1
if num2 < menor:
    menor = num2

if num3 < menor:
    menor = num3

#saída
print("o menor deles é ", menor)