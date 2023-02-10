#Código para receber números maiores ou iguais a zero até receber um negativo e retornar quais \\
#têm dois dígitos significativos na ordem inversa que foram digitados
numeros =[]

N = int(input("Insira um número, negativos param: "))

while N >= 0:
    if N > 9 and N < 100:
        numeros.append(N)
    N = int(input("Insira um número, negativos param: "))

print("Os números com dois dígitos significativos são: ")

#Prof
'''numeros.reverse()
print(numeros)'''

#Teste bem sucedido
print(numeros[::-1])