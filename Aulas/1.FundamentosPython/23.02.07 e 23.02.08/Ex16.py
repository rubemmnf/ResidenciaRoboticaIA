num = int(input("Insira um número inteiro positivo:"))
somaDivs = 0

while (num <= 0):
    num = int(input("Inválido. Insira um número inteiro positivo:"))

for i in range(1, num):
    if num % i == 0:
        somaDivs += i

if num == somaDivs:
    print("É perfeito")
else:
    print("Não é perfeito")