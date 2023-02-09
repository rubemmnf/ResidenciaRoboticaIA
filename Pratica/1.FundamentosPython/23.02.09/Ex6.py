#Código para receber uma quantidade N de números e separar os pares dos ímpares

#Entrada

N = int(input("Insira o valor de N: "))
numerosInformados = []
impares = []
pares = []

while N <= 0:
    N = int(input("Inválido. Insira o valor de N: "))

for num in range(N):
    num = int(input("Insira o número: "))
    numerosInformados.append(num)

#Solução
for num in numerosInformados:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

#Saída
print("Os números informados foram: ", numerosInformados)
print("Os números pares são", pares)
print("Os números ímpares são",impares)