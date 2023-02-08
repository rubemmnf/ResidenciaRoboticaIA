num = int(input("Insira um número inteiro positivo:"))
raiz = 0
d = 2

while d<= raiz and num % d != 0:
    d = d + 1

if d > raiz:
    print(num, 'é primo')
else:
    print(num, 'não é primo', d, 'é um divisor')